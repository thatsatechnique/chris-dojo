from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "This is the web service. Flag is not here!"