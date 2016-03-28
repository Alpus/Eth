#!env/bin/python3.4

from flask import Flask
from flask.ext.assets import Environment, Bundle
from flask.ext.sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')
manager = Manager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

assets = Environment(app);
css = Bundle('scss/materialize.scss', filters='pyscss', output='css/all.css')
assets.register('all_css', css)
js = Bundle('js/*', filters='jsmin', output='js/all.js')
assets.register('all_js', js)

if __name__ == "__main__":
    manager.run()

from app import views, models