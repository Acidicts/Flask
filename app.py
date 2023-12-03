from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Hello")

@app.route("/8YB")
def home():
    return render_template()
