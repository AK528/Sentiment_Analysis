from flask import Flask , make_response, jsonify, request
from sentiment_analysis import utility
from sentiment_analysis.preprocessor import preprocessing
from sentiment_analysis.feature_extraction import feature_extraction
from sentiment_analysis.config import sentiment_class


app = Flask(__name__)
model = utility.load_instance('./sentiment_analysis/saved_instance/model')
vectorizer = utility.load_instance('./sentiment_analysis/saved_instance/vectorizer')
preprocess = preprocessing.PreProcessor()
feature = feature_extraction.FeatureExtraction()
class_dict = preprocess.sentiment_label(sentiment_class)


@app.route('/', methods=['GET', 'POST'])
def sentiments():

    if request.method == 'POST':
        phrase = request.form['phrase']
        processed = preprocess.lemmatize(phrase)
        data = feature.make_prediction(vectorizer, [processed])
        prediction = model.predict(data)
        sentiment = prediction.tolist()
        prediction = class_dict[sentiment[0]]

        return make_response(jsonify({'sentiment': prediction}), 200)

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post>
      <input type=text name=phrase>
      <input type=submit>
    </form>
    '''


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5000)

