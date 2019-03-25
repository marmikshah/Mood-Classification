from flask import Flask, flash, redirect, render_template, request, session, abort
from pipeline import Pipeline

app = Flask(__name__)

# Home Page
@app.route("/")
def index():
    return render_template("index.html")

# Classifier Function
@app.route('/classify', methods=['POST'])
def handle_data():
    # Get Lyrics
    lyrics = request.form['lyrics']

    if not lyrics :
        return "No Lyrics Found!"
    # Convert to list if it is not.
    if type(lyrics) == type("") :
        lyrics = [lyrics]

    # Instantiate a pipeline object
    pipeline = Pipeline(lyrics);

    # Get the results.
    return pipeline.vectorize()

# Main Function
if __name__ == "__main__":
    # Run the Flask Server
    app.run()
