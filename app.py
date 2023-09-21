from flask import Flask, render_template, request
import pickle
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Load the models and CountVectorizer
with open('naive_bayes_model.pkl', 'rb') as file:
    nb_classifier = pickle.load(file)

with open('logistic_regression_model.pkl', 'rb') as file:
    logistic_classifier = pickle.load(file)

with open('random_forest_model.pkl', 'rb') as file:
    rf_classifier = pickle.load(file)

with open('count_vectorizer.pkl', 'rb') as file:
    cv = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/<model_name>', methods=['GET', 'POST'])
def predict(model_name):
    if request.method == 'POST':
        keyword = request.form['keyword']
        keyword_count = cv.transform([keyword])

        if model_name == 'naive_bayes':
            prediction = nb_classifier.predict(keyword_count)
        elif model_name == 'logistic':
            prediction = logistic_classifier.predict(keyword_count)
        elif model_name == 'random_forest':
            prediction = rf_classifier.predict(keyword_count)
        else:
            prediction = None

        sentiment = 'Positive' if prediction[0] == 2 else 'Negative' if prediction[0] == 0 else 'Neutral'

        return render_template('result.html', model_name=model_name, sentiment=sentiment)
    else:
        # Handle GET request (when the user first accesses the page)
        return render_template('result.html', model_name=model_name, sentiment=None)

if __name__ == '__main__':
    app.run(debug=True)
