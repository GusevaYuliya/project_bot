from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd
import matplotlib.pyplot as plt

Y_0 = []
X_0 = []
with open("data.txt") as f:
    for i in range(127):
        l = f.readline()
        L = l.split()
        y = int(L[0])
        x = [int(k) for k in L[1:]]
        Y_0.append(y)
        X_0.append(x)
X = np.array(X_0)
Y = np.array(Y_0)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)
grid = {'n_estimators': np.arange(1, 105, 5), 'max_features': ['auto', 'sqrt', 'log2']}
randomforest = RandomForestClassifier()
grid_randomforest = GridSearchCV(randomforest, grid, cv=10)
grid_randomforest.fit(X_train, Y_train)

print("tuned hpyerparameters :(best parameters) ", grid_randomforest.best_params_)
print("accuracy :", grid_randomforest.best_score_ * 100)

randomforest = RandomForestClassifier(grid_randomforest.best_params_)
grid_randomforest.fit(X, Y)


def pred(XX):
    X_t = np.array([XX])
    predictions = grid_randomforest.predict(X_t)
    return predictions[0]
