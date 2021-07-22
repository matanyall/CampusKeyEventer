from flask import Flask, request, render_template, session
from pathlib import Path
debug=True # set this to false later;
app = Flask(__name__)
from models import Event
import json

# Most safe practice amirite...
secret_key_file = 'flask_key.txt'
with open(secret_key_file) as f:
    app.secret_key = f.read()

@app.route("/")
def index():
    session['page'] = 'Welcome'
    return render_template(str(Path("index.html")))

@app.route("/events")
def events():
    session['page'] = 'Events'
    # Get all events
    path = str(Path("./events.json"))
    events = None
    with open(path) as json_file:
        events = json.load(json_file)
    session['events'] = events['events']
    return render_template(str(Path('events.html')))
