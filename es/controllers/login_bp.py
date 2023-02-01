from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user

from .forms import LoginForm
from ..models import UsersModel
from es.config import login_manager


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return UsersModel.query.get(int(user_id))
    return None


login = Blueprint('login', __name__)


@login.route('/login', methods=['POST', 'GET'])
def login_func():
    if current_user.is_authenticated:
        return redirect(url_for('common.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = UsersModel.query.filter_by(login=form.login.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('common.index'))
        else:
            flash('Неверный логин или пароль.', category='danger')
    return render_template('login.html', form=form)


@login.route('/logout', methods=['POST', 'GET'])
def logout_func():
    logout_user()
    return redirect(url_for('login.login_func'))
