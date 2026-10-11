import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import pickle
from sklearn.metrics import mean_squared_error as mse, r2_score as r2

df = pd.read_excel('./Data/Data_final.xlsx')

df.dropna(inplace = True)

X = df.drop(columns = 'Fr')
Y = df['Fr']

X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size= 0.2, random_state=42)

model = XGBRegressor()

model.fit(X_train, y_train)

print(f'mse : {mse(y_test, model.predict(X_test)) : 0.4f}')
print(f'r2 score : {r2(y_test, model.predict(X_test)) : 0.4f}')

df['predicted'] = model.predict(X)

df.to_excel('xgboost_predicted.xlsx', index = False)
