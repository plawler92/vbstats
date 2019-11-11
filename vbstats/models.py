from sqlalchemy import Column, Integer, String, Date
#from vbstats.database import Base
from vbstats import db

player_teams = db.Table('playerteams',
    db.Column('player_id', db.Integer, db.ForeignKey('player.id'), primary_key=True),
    db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True)
)

# player_game = db.Table('playergames',
#     db.Column('player_id', db.Integer, db.ForeignKey('player.id'), primary_key=True),
#     db.Column('game_id', db.Integer, db.ForeignKey('game.id'), primary_key=True),
#     db.Column('going', db.Boolean)
# )

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    gender = db.Column(db.String(1))

    games = db.relationship("Game", secondary="player_game_link")

    def __init__(self, name=None, gender=None):
        self.name = name
        self.gender = gender

    def __repr__(self):
        return f'<Player: {self.name}, {self.gender}>'

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(50))
    gamedate = db.Column(db.Date)
    gamenumber = db.Column(db.Integer)
    #Attack
    kills = db.Column(db.Integer)
    attackerrors = db.Column(db.Integer)
    totalattacks = db.Column(db.Integer)
    #Settings
    assists = db.Column(db.Integer)
    settingerrors = db.Column(db.Integer)
    #Service
    aces = db.Column(db.Integer)
    serveattempts = db.Column(db.Integer)
    serveerrors = db.Column(db.Integer)
    #Passing
    receiveattempts = db.Column(db.Integer)
    receiveerrors = db.Column(db.Integer)
    #Defense
    digs = db.Column(db.Integer)
    digerrors = db.Column(db.Integer)
    #Blocking
    blocks = db.Column(db.Integer)
    blockassists = db.Column(db.Integer)
    blockerrors = db.Column(db.Integer)

    def __init__(self, player=None, gamedate=None, 
                 kills=None,attackerrors=None,totalattacks=None,
                 assists=None,settingerrors=None,
                 aces=None,serveattempts=None,serveerrors=None,
                 receiveattempts=None,receiveerrors=None,
                 digs=None,digerrors=None,
                 blocks=None,blockassists=None,blockerrors=None):
        self.player = player
        self.gamedate = gamedate
        self.kills = kills
        self.attackerrors = attackerrors
        self.totalattacks = totalattacks
        self.assists = assists
        self.settingerrors = settingerrors
        self.aces = aces
        self.serveattempts = serveattempts
        self.serveerrors = serveerrors
        self.receiveattempts = receiveattempts
        self.receiveerrors = receiveerrors
        self.digs = digs
        self.digerrors = digerrors
        self.blocks = blocks
        self.blockassists = blockassists
        self.blockerrors = blockerrors

    def __repr__(self):
        return f'<Stats: {self.player}, {self.gamedate}>'

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(50))
    time = db.Column(db.DateTime)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team = db.relationship('Team')

    players = db.relationship("Player", secondary="player_game_link")

    def __init__(self, location=None, time=None):
        self.location = location
        self.time = time
    
    def __repr__(self):
        return f'<Game: {self.location}, {self.time}, {self.team_id}>'

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    players = db.relationship('Player', secondary=player_teams)
    games = db.relationship('Game')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return f'<Team: {self.name}>'

class PlayerGameLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))

    going = db.Column(db.Boolean)

    player = db.relationship(Player)
    game = db.relationship(Game)



