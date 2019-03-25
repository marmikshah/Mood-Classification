from flask import Flask, flash, redirect, render_template, request, session, abort
from pipeline import Pipeline

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/classify', methods=['POST'])
def handle_data():
    lyrics = request.form['lyrics']
    return Pipeline(lyrics);

if __name__ == "__main__":
    app.run()
