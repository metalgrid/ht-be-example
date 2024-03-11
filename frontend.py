from flask import Blueprint, send_from_directory, send_file

frontend = Blueprint("frontend", __name__)


@frontend.route("/")
def index():
    return send_file("public/index.html")


@frontend.route("/css/<path:path>")
def send_css(path):
    return send_from_directory("public/css", path)


@frontend.route("/js/<path:path>")
def send_js(path):
    return send_from_directory("public/js", path)
