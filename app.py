from flask import Flask

from api import api
from frontend import frontend

app = Flask(__name__)

app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(frontend)
