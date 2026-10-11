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

X_train.to_excel('Data/Train test split/X_train.xlsx', index = False)
X_test.to_excel('Data/Train test split/X_test.xlsx', index = False)
y_train.to_excel('Data/Train test split/y_train.xlsx', index = False)
y_test.to_excel('Data/Train test split/y_test.xlsx', index = False)