import json
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)
data = json.load(open(str(Path("api", "links.json"))))


@app.route("/", methods=["GET"])
def home():
    return render_template(
        "index.html",
        external_links=data.get("external_links"),
        projects=data.get("projects"),
    )


@app.route("/license", methods=["GET"])
def license():
    return render_template("license.html")


@app.route("/terms", methods=["GET"])
def terms_of_service():
    return render_template("terms.html")


@app.route("/privacy", methods=["GET"])
def privacy():
    return render_template("privacy.html")
