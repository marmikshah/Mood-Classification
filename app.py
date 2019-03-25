from flask import Flask, flash, redirect, render_template, request, session, abort
from pipeline import Pipeline

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/classify', methods=['POST'])
def handle_data():
    lyrics = request.form['lyrics']
    pipeline = Pipeline(lyrics);
    return pipeline.vectorize()

if __name__ == "__main__":
    app.run()
