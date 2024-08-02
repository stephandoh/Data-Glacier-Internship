from flask import Flask, jsonify, request
import pickle
import pandas as pd

# Creating a Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        data = "hello world"
        return jsonify({'data': data})

@app.route('/predict/')
def price_predict():
    model = pickle.load(open('model.pickle', 'rb'))
    income = request.args.get('income')
    house_age = request.args.get('house_age')
    rooms = request.args.get('rooms')
    bedrooms = request.args.get('bedrooms')
    population = request.args.get('population')

    test_df = pd.DataFrame({
        'Avg. Area Income': [income],
        'Avg. Area House Age': [house_age],
        'Avg. Area Number of Rooms': [rooms],
        'Avg. Area Number of Bedrooms': [bedrooms],
        'Area Population': [population]
    })

    pred_price = model.predict(test_df)
    return jsonify({'House Price': str(pred_price[0])})

if __name__ == '__main__':
    app.run(debug=True)
