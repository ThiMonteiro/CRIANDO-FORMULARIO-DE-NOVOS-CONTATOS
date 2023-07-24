from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
app.config["SECRET_KEY"] = "a8cbxAjx!xZCAd7"

from app.controllers import default
