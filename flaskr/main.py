import requests, functools
from __init__ import create_app
from flask import Blueprint, render_template

if __name__ == '__main__':
    app = create_app()

    app.run('0.0.0.0')

bp = Blueprint('main', __name__, url_prefix="/")

@bp.route('/')
def main():
    r = requests.get("https://api.mcsrvstat.us/2/kieroth29.xyz")
    r = r.json()

    return render_template("main.html", r=r)