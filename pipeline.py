from sklearn.svm import SVC, LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle;

class Pipeline(object) :
    def __init__(self, lyrics) :
        self.lyrics = lyrics;

    def vectorize(self) :
        vectorizer = pickle.load(open("vectorizer.tfidf", "rb"));

        return self.predict(vectorizer.transform(self.lyrics));

    def predict(self, x) :
        model = pickle.load(open("model.svm","rb"))
        y = model.predict(x)[0];
        if y == 0 :
            return "Sad"
        return "Happy";
        