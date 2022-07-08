from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import os
import pandas as pd

# chdir to data
data_folder_name = "data";
os.chdir(os.getcwd() + "\\1-machine_models\\" + data_folder_name);

file = pd.read_csv('music.csv');
x = file.drop(columns=['genre']);
y = file['genre'];

# build model
model = DecisionTreeClassifier();
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=.3);
model.fit(X_train, y_train);

# predict
print(X_test);
prediction = model.predict(X_test);
# score
print(y_test);
score = accuracy_score(y_test, prediction);
print(score)