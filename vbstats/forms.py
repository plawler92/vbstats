from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired
from vbstats.models import Player

class TeamForm(FlaskForm):
    name = StringField('Team Name', validators=[DataRequired()])
    submit = SubmitField('Add Team')

class TeamAddPlayerForm(FlaskForm):
    players = Player.query.all()
    choices = []
    choices.append(('', ''))
    for player in players:
        choices.append((player.id, player.name))
    player = SelectField('Add Player', choices=choices)
    submit = SubmitField('Add')

class PlayerForm(FlaskForm):
    name = StringField('Player Name', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F','Female')], validators=[DataRequired()])
    submit = SubmitField('Add Player')

