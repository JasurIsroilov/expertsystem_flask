from flask_login import UserMixin

from es.config import db, user_roles


class UsersModel(db.Model, UserMixin):

    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def __init__(self, login, password, role):
        self.login = login
        self.password = password
        self.role = role

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def edit_user(old_user, form):
        old_user.login = form.login.data
        old_user.password = form.password.data
        old_user.role = user_roles.get(form.role.data)
        db.session.commit()

    @classmethod
    def delete_user(cls, user_id):
        old_user = cls.query.get_or_404(user_id)
        db.session.delete(old_user)
        db.session.commit()
