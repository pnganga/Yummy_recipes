import os
from flask_login import LoginManager
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views

