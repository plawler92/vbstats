from sqlalchemy import Column, Integer, String, Date
#from vbstats.database import Base
from vbstats import db

class Stats(db.Model):
    #__tablename__ = 'stats'
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(50))
    gamedate = db.Column(db.Date)
    gamenumber = db.Column(db.Integer)
    #genereal
    dumberrors = db.Column(db.Integer)
    firstorsecondover = db.Column(db.Integer)
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

    def __init__(self, player=None, gamedate=None, dumberrors=None,firstorsecondover=None,
                 kills=None,attackerrors=None,totalattacks=None,
                 assists=None,settingerrors=None,
                 aces=None,serveattempts=None,serveerrors=None,
                 receiveattempts=None,receiveerrors=None,
                 digs=None,digerrors=None,
                 blocks=None,blockassists=None,blockerrors=None):
        self.player = player
        self.gamedate = gamedate
        self.dumberrors = dumberrors
        self.firstorsecondover = firstorsecondover
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