from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os.path
from flask_login import LoginManager
from flask_cors import CORS


from sqlalchemy import *
def mkpath(p):
    return os.path.normpath(os.path.join(os.path.dirname( __file__ ),p))


app = Flask( __name__ )
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../myapp.db'))
login_manager = LoginManager(app)
login_manager.login_view = "login"
db = SQLAlchemy(app)
CORS(app)