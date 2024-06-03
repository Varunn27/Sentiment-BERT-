from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
from model.getPredictions import get_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

percent_dict = {}

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        input_text = request.form['text']
        blob = TextBlob(input_text)
        if len(input_text) < 50:
            sentiment, percent_dict = get_sentiment(input_text)
        else:
            sentiment, percent_dict = None, None
        print(sentiment)
        return render_template('result.html', FinalPrediction=sentiment, Percentages=percent_dict, Text=input_text)

@app.route('/get-percentages', methods=['GET'])
def get_percentages():
    percent_dict = { "a": "b", "c" : "d"}
    return jsonify(percent_dict)

if __name__ == '__main__':
    app.run(debug=True)
