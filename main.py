import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    r = requests.get("https://api.mcsrvstat.us/2/kieroth29.xyz")
    r = r.json()

    return render_template("main.html", r=r)

if __name__ == '__main__':
    app.run('0.0.0.0')