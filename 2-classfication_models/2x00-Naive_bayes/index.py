from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import os

# change directory to working

os.chdir(os.getcwd() + "\\" + "2-classification_models\data")
data = pd.read_csv('tested.csv')
print(data.head)