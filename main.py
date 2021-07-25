import requests, os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
   r = requests.get("https://api.mcsrvstat.us/2/kieroth29.xyz")
   r = r.json()

   return render_template("main.html", r=r)

if __name__ == '__main__':
   context = (os.environ.get('CERT_FILE'), os.environ.get('CERT_PW'))
   app.run('0.0.0.0', ssl_context=context)
