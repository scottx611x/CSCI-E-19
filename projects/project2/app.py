from flask import Flask, jsonify

from utils import MessageConstructor

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name="world"):
    if name == "super_secret":
        message = f'You found the secret, good job!'
    else:
        message = f'Hello {name.title()}!'
    return jsonify(
        MessageConstructor(message).message
    )

