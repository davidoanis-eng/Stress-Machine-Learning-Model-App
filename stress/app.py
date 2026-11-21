# build an interface for model testing
# import the necessary libraries
from flask import Flask, request, jsonify, render_template
import pickle

# load the model
with open('stress_model.pkl', 'rb') as f:
    model = pickle.load(f)

# create the flask app
app = Flask(__name__)

# define the home route
@app.route('/')
def home():
    return render_template('index.html')   

# define the predict route
@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('text', '').strip()
    if not text:
        return jsonify({'error': 'Please enter some text to analyze.'}), 400

    prediction = model.predict([text])
    return jsonify({'prediction': str(prediction[0])})

# run the app
if __name__ == '__main__':
    app.run(debug=True)