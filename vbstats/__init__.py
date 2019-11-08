"""
the flask application package.
"""

from flask import Flask
from vbstats.config import Config
#from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

#import vbstats.views
#import vbstats.views
#import vbstats.models
from vbstats import views, models