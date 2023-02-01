from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length

from ..config import user_roles


class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class UserForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired(), Length(min=2, max=50)])
    password = StringField('Пароль', validators=[DataRequired(), Length(min=2, max=50)])
    role = SelectField('Роль', choices=list(user_roles.keys()))
    submit = SubmitField('ОК')


class SlotsForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired(), Length(min=2, max=50)])
    description = TextAreaField('Описание', validators=[DataRequired(), Length(min=2, max=300)])
    submit = SubmitField('ОК')


class FramesForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    parent = SelectField('Родитель')
    is_instance = BooleanField('Экземпляр')
    submit = SubmitField('ОК')


class SlotValueForm(FlaskForm):
    value = StringField('Значение слота', validators=[DataRequired(), Length(min=2, max=300)])
    submit = SubmitField('Ок')


class SlotsFramesForm(FlaskForm):
    slv_value = SelectField('Значение слота')
    slt_name = SelectField('Экземпляры')
    submit = SubmitField('Ок')


class SintezForm(FlaskForm):
    slt_name = StringField('Значение слота')
    slv_val = SelectField('Выберите вариант')
    submit = SubmitField('Дальше')
