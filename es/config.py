import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
login_manager = LoginManager()

user_roles = {
    'Администратор': 'admin',
    'Эксперт': 'expert',
    'Технолог': 'tech'
}


class Config:
    SECRET_KEY = '5e6775a88eccfdceaa3e6f6717a9cad1'
    SQLALCHEMY_DATABASE_URI = 'oracle://JASUR:JASUR@localhost:1521/xe'
