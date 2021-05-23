from flask import *
from markupsafe import escape
from device import feedOn, feedOff, latestDataRetrieve, allDataRetrieve
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content_Type"


@app.route("/")
def hello():
    return "<h1> You're accessing Smart Garden API </h1>"


@app.route("/api/test/data", methods=["GET"])
def data():
    isLastest = request.args.get("latest")
    if isLastest in ["TRUE", "True", "true"] or isLastest == None:
        return latestDataRetrieve()
    elif isLastest in ["FALSE", "False", "false"]:
        print(allDataRetrieve())
        return allDataRetrieve()
    else:
        return f"Couldn't work with latest = {isLastest}"


@app.route("/api/test", methods=["GET"])
def actionRoute():
    # param is the action you want to do with device
    param = request.args.get("param")
    if param == "ON" or param == "on" or param == "On":
        return feedOn()
    elif param == "OFF" or param == "Off" or param == "off":
        return feedOff()
    else:
        return f"Couldn't work with param = {param}"
