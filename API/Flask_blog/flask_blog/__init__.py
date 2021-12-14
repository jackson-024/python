from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc90955c1ea67d182824cbb6d3c7d35c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://v2:Jackson24@localhost/v2-python'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from flask_blog import routes