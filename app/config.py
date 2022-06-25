from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_migrate import Migrate
from flask_login import LoginManager
from os import getenv


SQLALCHEMY_DATABASE_URL = getenv('DATABASE_URL', 'postgresql://user:password@host/db_name')
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
admin = Admin()


def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@host/db_name'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    return app
