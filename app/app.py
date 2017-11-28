from flask import Flask

from routes import *


app = Flask(__name__)

app.register_blueprint(route.api)