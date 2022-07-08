from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import os

(os.chdir(os.getcwd() + "\\" + "3-regression\data\\archive"))

data = pd.read_csv('HousingData.csv');
# fill null with average
data = data.fillna(data.mean())

x = data[['LSTAT','RM','NOX','PTRATIO','DIS','AGE']]
y = data['MEDV']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=.3, random_state=102)

model = LinearRegression()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
score = model.score(X_train, y_train)
print(score)