from vbstats import db
from vbstats.models import Player, PlayerGameLink, Team, Game
from datetime import datetime

p1 = Player(name="mexico", gender="m")
p2 = Player(name="stephanie", gender="f")

t1 = Team(name="spikel jordan") #add players, games

g1 = Game(location="st andrews", time=datetime.today())

t1.games.append(g1)

db.session.add(t1)
db.session.commit()

# pgl1 = PlayerGameLink(player=p1, game=g1, going=True)
# pgl2 = PlayerGameLink(player=p2, game=g1, going=False)

#x = PlayerGameLink.query.filter(PlayerGameLink.going == True).all()