import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import scipy
from scipy.optimize import minimize_scalar
from mpl_toolkits import mplot3d

def Jlogbiaslinmodel(X,Y):
    def Jmodel(b):
        z = Y-b
        if np.any(z <= 0):
            return np.inf
        k, intercept = np.polyfit(X,np.log(z),1)
        Ypredbias = np.exp(k*X+intercept) + b
        return np.sum((Y-Ypredbias)**2)
    return Jmodel
