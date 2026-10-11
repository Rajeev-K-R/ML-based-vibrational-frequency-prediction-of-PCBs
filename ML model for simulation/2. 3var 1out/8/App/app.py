from flask import Flask, render_template, request, session, redirect, url_for
from sklearn.ensemble import RandomForestRegressor
import xgboost
import pickle
import numpy as np


model_path = './Models/XGBR-GSCV.pkl'
model = None

with open(model_path, 'rb') as f:
    model = pickle.load(f)


app = Flask(__name__)

app.secret_key = 'v1.0'

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
            val3 = float(request.form.get('val3'))

            res = model.predict(np.array([[val1, val2, val3]]))[0]
            res = np.round(float(res),3)
        except:
            errormsg = "Please type valid input"
        
        session['last result'] = res

        return redirect(url_for('home'))
    
    res = session.pop('last result',None)

    return render_template('index.html', result = res, error = errormsg)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = True)
