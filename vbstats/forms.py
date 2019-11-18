from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, SelectField, DateTimeField, DateField
from wtforms.validators import DataRequired
from flask_admin.form.widgets import DatePickerWidget
from vbstats.models import Player

class TeamForm(FlaskForm):
    name = StringField('Team Name', validators=[DataRequired()])
    submit = SubmitField('Add Team')

class TeamAddPlayerForm(FlaskForm):
    player = SelectField('Add Player')
    submit = SubmitField('Add')

    def __init__(self):
        super().__init__()
        players = Player.query.all()
        choices = []
        choices.append(('', ''))
        for player in players:
            choices.append((player.id, player.name))
        self.player.choices=choices

class PlayerForm(FlaskForm):
    name = StringField('Player Name', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F','Female')], validators=[DataRequired()])
    submit = SubmitField('Add Player')

class DeleteTeamForm(FlaskForm):
    submit = SubmitField('Delete Team')

class AddGameForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired()])
    time = StringField('Time')
    submit = SubmitField('Add Game')
    
