from flask import Blueprint

web = Blueprint("web", __name__)

@web.route("/")
def show():
    return "Hello world"