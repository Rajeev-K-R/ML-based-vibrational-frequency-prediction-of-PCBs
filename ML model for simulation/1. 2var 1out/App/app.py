from flask import Flask, render_template, request
from sklearn.ensemble import RandomForestRegressor
import pickle
import numpy as np


model_path = './Models/RFReg.pkl'
model = None

with open(model_path, 'rb') as f:
    model = pickle.load(f)


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    res = None
    errormsg = None

    if model is None:
        return render_template('index.html', result = res, error = 'Model import unsuccessful')
    

    if request.method == 'POST':
        try:
            val1 = float(request.form.get('val1'))
            val2 = float(request.form.get('val2'))

            res = np.round(model.predict(np.array([[val1, val2]]))[0],3)
        except:
            errormsg = "Please type valid input"
        
        

    return render_template('index.html', result = res, error = errormsg)

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8000, debug = True)
