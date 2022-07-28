from flask import Flask
from pun import compute
import json

app = Flask(__name__)

@app.route("/generate/non_recursive/")
def pun():
    return json.dumps(compute("eye of the tiger".split(), 'lev', 10, False))