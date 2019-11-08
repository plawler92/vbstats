"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from vbstats import app, db
from vbstats.common import get_stats
from vbstats.models import Stats

@app.route('/', methods=['GET','POST'])
@app.route('/stats', methods=['GET','POST'])
def stats():
    """Renders the home page"""
    players = ["mexico", "stephanie"]
    stats_master_list = get_stats()

    if request.method == 'POST':
        print("hello")
        print(request.form)
        stat_list = []
        for player in players:
            s = Stats()
            s.player = player
            s.gamedate = datetime.strptime(request.form['gamedate'], '%Y-%m-%d').date()
            s.gamenumber = 1
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