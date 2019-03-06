# This code does not work!
# please watch section video for explanation of what was typed
# THIS CODE DOES NOT WORK

import os
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

votes = {"yes": 0, "no": 0, "maybe": 0}

channels = { }


@app.route("/")
def index():
    return render_template("index.html", votes=votes)


@socketio.on("sned-message")
def msg(data):
	data["msg"]
	data["channel"]
