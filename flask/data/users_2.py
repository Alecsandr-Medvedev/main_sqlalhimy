from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, FloatField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    job = TextAreaField('Работа', validators=[DataRequired()])
    team_leader = IntegerField('Лидер', validators=[DataRequired()])
    work_size = FloatField("Время затраченное на работу", validators=[DataRequired()])
    collaborators = TextAreaField("Список участников", validators=[DataRequired()])
    is_finish = remember_me = BooleanField('Закончена ли работа')
    submit = SubmitField('Добавить работу')
