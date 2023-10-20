import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]

    # Transform the features using the scaler and encoder
    scaled_features = scaler.transform(final_features)
    encoded_features = encoder.transform(scaled_features)

    prediction = model.predict(encoded_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='GVHD prediction {}'.format(output))

@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    For direct API calls through request
    '''
    data = request.get_json(force=True)

    # Transform the data using the scaler and encoder
    data = np.array(list(data.values()))
    scaled_data = scaler.transform([data])
    encoded_data = encoder.transform(scaled_data)

    prediction = model.predict(encoded_data)

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
