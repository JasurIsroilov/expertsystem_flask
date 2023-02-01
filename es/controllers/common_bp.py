from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

from ..models import UsersModel


common = Blueprint('common', __name__)


@common.route('/')
@common.route('/index')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login.login_func'))
    rows = UsersModel.query.all()
    return render_template('index.html', rows=rows)
