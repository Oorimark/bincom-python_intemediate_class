from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as snb

from util import cleaner

# change directory to working
os.chdir(os.getcwd() + "\\2-classfication_models\data")
data = pd.read_csv('tested.csv')
cleaner = cleaner(data)
print(data.head)
print(data.drop(['Sex']))

def clean_age(data: dict):
    cleaned = data['Age'].fillna(data['Age'].mean())
    return cleaned

cleaner.isnull_avg(['Age'])
print(cleaner.get_cleaned_data())