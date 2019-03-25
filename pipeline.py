from sklearn.svm import SVC, LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle;

class Pipeline(object) :
    def __init__(self, lyrics) :
        if type(lyrics) == type(""):
            # Convert to list (this is what the classifier predict fn will take as input).
            lyrics = [lyrics]
        return self.vectorize(lyrics);

    def vectorize(self, lyrics) :
        vectorizer = pickle.load(open("vectorizer.tfidf", "rb"));

        return self.predict(vectorizer.tranform(lyrics));

    def predict(self, x) :
        model = pickle.load(open("model.svm","rb"))
        y = model.predict(x).pop();
        if y == 0 :
            return "Sad"
        return "Happy";
        