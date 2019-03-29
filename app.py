from flask import Flask, flash, redirect, render_template, request, session, abort
from pipeline import Pipeline
from musixmatch.api import Musix, Track;
from ibm.tone import ToneAnalyzer;

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


@app.route("/musixmatch",methods=['POST'])
def musixmatch() :
    k = int(request.form['k'])
    country = request.form['country']
    musix = Musix(country)
    tracks = musix.get_top_lyrics(k)

    result = ""
    for track in tracks :
        try :
            pipeline = Pipeline([track.lyrics])
            track.label(pipeline.vectorize())

            ibm = ToneAnalyzer();
            imb_results = ibm.analyze(track);
            result = result + (track.name + " by <i>" + track.artist + "</i> : <b><u>" + track.mood + "</b></u> || IBM's Results <b><u>" + ', '.join(imb_results)) + "</b></u><br><br>"

        except AttributeError :
            pass

    return render_template("musixmatch.html", k=k, result=result)

# Main Function
if __name__ == "__main__":
    # Run the Flask Server
    app.run()
