from flask import render_template

from app import app
from app.models.info import Info


@app.route("/")
def form():
    info = Info()
    return render_template("forms.html", info=info)

