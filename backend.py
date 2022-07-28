from flask import Flask, request
from pun import compute
import json
import html

app = Flask(__name__)

@app.route("/generate/non_recursive")
def pun():
    user_input = request.args.get('input')

    return json.dumps(user_input)
#     return json.dumps(compute("eye of the tiger".split(), 'lev', 10, False))