from flask import Flask, request, render_template, session
from pathlib import Path
debug=True # set this to false later;
app = Flask(__name__)
from models import Event
# from main import *

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
    return render_template(str(Path('events.html')))


@app.route('/events/cornhusking')
def cornhusking():
    session['page'] = 'Cornhusking'
    return render_template(str(Path('cornhusking.html')))

@app.route('/map')
def map():
    session['page'] = 'Map'
    return render_template(str(Path('map.html')))

@app.route('/events/cornhusking/qr')
def qr():
    session['page'] = 'QR Code'
    return render_template(str(Path('qr.html')))

