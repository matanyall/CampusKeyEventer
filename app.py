from flask import Flask, request, render_template, session
from pathlib import Path

app = Flask(__name__)

# Most safe practice amirite...
app.secret_key = 'nelnet'

@app.route("/")
def index():
    session['page'] = 'Map'
    return render_template(str(Path("index.html")))