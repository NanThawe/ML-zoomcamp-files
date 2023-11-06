import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

# with open('dv.pkl', 'rb') as f_in:
#     dv = pickle.load(f_in)
# with open(model_file, 'rb') as f_in:
#     model = pickle.load(f_in)

app = Flask('dropout')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    student = request.get_json()

    X = dv.transform([student])
    y_pred = model.predict_proba(X)[0, 1]
    rate = y_pred * 100

    result = {
        'dropout_probability': float(y_pred),
        'rate': int(rate)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)