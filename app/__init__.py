from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

import os

APP_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_FOLDER = os.path.join(APP_DIR, '../static/dist') # Where your webpack build output folder is
TEMPLATE_FOLDER = os.path.join(APP_DIR, '../static/public') # Where your index.html file is located

app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)
app.config.from_object('app.settings')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)