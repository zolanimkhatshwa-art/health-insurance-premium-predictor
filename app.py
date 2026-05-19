
from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('premium_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    age      = int(request.form['age'])
    sex      = int(request.form['sex'])
    bmi      = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker   = int(request.form['smoker'])
    region   = int(request.form['region'])

    sample = pd.DataFrame([[age, sex, bmi, children, smoker, region]],
             columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

    prediction = model.predict(sample)[0]

    if prediction < 10000:
        risk = 'Low Risk'
    elif prediction < 20000:
        risk = 'Medium Risk'
    else:
        risk = 'High Risk'

    return render_template('index.html',
        prediction=f"${prediction:,.2f}",
        risk=risk)

if __name__ == "__main__":
    app.run(debug=True)
