from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired

class TeamForm(FlaskForm):
    name = StringField('Team Name', validators=[DataRequired()])
    submit = SubmitField('Add Team')

class PlayerForm(FlaskForm):
    name = StringField('Player Name', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F','Female')], validators=[DataRequired()])
    submit = SubmitField('Add Player')
