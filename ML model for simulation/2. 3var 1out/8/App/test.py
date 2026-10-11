import xgboost
import pickle
import numpy as np


model_path = './Models/XGBReg-2.pkl'
model = None

with open(model_path, 'rb') as f:
    model = pickle.load(f)


res = np.round(model.predict(np.array([[1, 45, 55]]))[0],3)

print(res)
