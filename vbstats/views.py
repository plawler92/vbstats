"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect
from vbstats import app, db
from vbstats.common import get_stats
from vbstats.models import Stats, Player, Team
from types import SimpleNamespace
from vbstats.forms import TeamForm, PlayerForm

@app.route('/', methods=['GET','POST'])
@app.route('/stats', methods=['GET','POST'])
def stats():
    """Renders the home page"""
    players = ["mexico", "stephanie"]
    stats_master_list = get_stats()

    if request.method == 'POST':        
        stat_list = []
        for player in players:
            s = Stats()
            s.player = player
            s.gamedate = datetime.strptime(request.form['gamedate'], '%Y-%m-%d').date()
            s.gamenumber = request.form['gamenumber']
            for stat in stats_master_list:
                setattr(s, stat.tag, request.form[player + '-' + stat.tag])

            db.session.add(s)
            stat_list.append(s)

        db.session.commit()
        print(stat_list)

    return render_template(
        'stats.html',
        players=players,
        stats=stats_master_list
    )

@app.route('/view')
def view():
    stat_list = Stats.query.all()
    #print(stat_list)
    for stat in stat_list:
        print(stat.player)
    stat_master = get_stats()
    return render_template(
        'view.html',
        stats=stat_list,
        master=stat_master
    )

@app.route('/players', methods=['GET', 'POST'])
def players():
    if request.method == 'POST':
        p = Player(name=request.form['playername'], gender=request.form['gender'])
        db.session.add(p)
        db.session.commit()

    players = Player.query.all()


    return render_template(
        'players.html',
        players=players
    )

@app.route('/createplayer', methods=['GET', 'POST'])
def createplayer():
    form = PlayerForm()
    if form.validate_on_submit():
        p = Player(name=form.name.data, gender=form.gender.data)
        db.session.add(p)
        db.session.commit()
        return redirect('/players')
    
    return render_template(
        'createplayer.html',
        title='Create a Player',
        form=form
    )

@app.route('/teams')
def teams():
    teams = Team.query.all()
    
    return render_template(
        'teams.html',
        teams=teams
    )

@app.route('/createteam', methods=['GET', 'POST'])
def createteam():   
    form = TeamForm()
    if form.validate_on_submit():
        t = Team(name=form.name.data)
        db.session.add(t)
        db.session.commit()
        return redirect('/teams')
    return render_template(
        'createteam.html',
        title='Create a Team',
        form=form
    )

@app.route('/team/<id>')
def team(id):
    team = Team.query.filter_by(id=id).first_or_404()
    return render_template(
        'team.html',
        team=team,
        tile = team.name
    )