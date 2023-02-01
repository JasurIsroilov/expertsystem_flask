from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required

from ..models import UsersModel
from .forms import UserForm, user_roles


user = Blueprint('users', __name__)


@user.route('/users/add', methods=['POST', 'GET'])
@login_required
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        new_user = UsersModel(login=form.login.data, password=form.password.data, role=user_roles[form.role.data])
        new_user.add_user()
        flash('Добавление успешно', category='success')
        return redirect(url_for('common.index'))
    return render_template('users/add.html', form=form)


@user.route('/users/edit', methods=['POST', 'GET'])
@login_required
def edit_user():
    bar = request.args.to_dict()
    old_user = UsersModel.query.get_or_404(bar.get('id'))
    form = UserForm()
    if form.validate_on_submit():
        UsersModel.edit_user(old_user, form)
        flash('Редактирование успешно', 'success')
        return redirect(url_for('common.index'))
    form.login.data = old_user.login
    form.role.data = old_user.role
    form.password.data = old_user.password
    return render_template('users/edit.html', form=form)


@user.route('/users/delete', methods=['GET', 'POST'])
@login_required
def delete_user():
    bar = request.args.to_dict()
    UsersModel.delete_user(bar.get('id'))
    flash('Удаление успешно', category='success')
    return redirect(url_for('common.index'))
