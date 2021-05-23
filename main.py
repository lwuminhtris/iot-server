from flask import Flask
from markupsafe import escape
from device import lightOn, lightOff, dataRetrieve
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content_Type"


@app.route("/")
def hello():
    return "<p> Hello </p>"


@app.route("/data")
def data():
    return dataRetrieve()


@app.route("/lightOn")
def turnOnLight():
    return lightOn()


# return "<p>Turn On the Light!!</p>"


@app.route("/lightOff")
def turnOffLight():
    return lightOff()
    # return "<p>Turn Off the Light</p>"


@app.route("/<name>")
def abc(name):
    return f"<h1>Error: {escape(name)} does not exist!</h1>"
