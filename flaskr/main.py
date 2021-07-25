import requests, functools

from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix="/")

@bp.route('/')
def main():
    r = requests.get("https://api.mcsrvstat.us/2/kieroth29.xyz")
    r = r.json()

    return render_template("main.html", r=r)