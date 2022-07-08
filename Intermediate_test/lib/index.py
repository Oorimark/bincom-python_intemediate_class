from dataclasses import dataclass
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

from lib.cleaner.index import data_cleaner
from util.index import InvalidOption
import pandas as pd

class data():
    train: any;
    test: any;
    X_train: any;
    X_test: any;
    y_train: any;
    y_test: any;
    
    def __init__(self, test, train) -> None:
        self.test = pd.read_csv(test)
        self.train = pd.read_csv(train)
    
    def load(self, train: any, test: any):
        self.test = test
    
    def split_train_test(self, deg: int) -> None:
        self.train.drop(['Loan_ID'], axis = 1 , inplace =True)
        X = self.train.drop('Loan_Status', axis = 1)
        y = self.train['Loan_Status']
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X,y, test_size= deg, random_state=105)

        
        ...
        
    def model(self, opt) -> int:
        if opt != '1' and opt != '2':
            InvalidOption()
        
        if opt == '1': # 1 -> RandomForestClassifier
            random_forest = RandomForestClassifier(n_estimators=100)
            random_forest.fit(self.X_train, self.y_train)
            predict = random_forest.predict(self.X_test)
            return accuracy_score(self.y_test, predict) * 100
        
        if opt == '2': # 2 -> Naive Bayes
            naive_baye = GaussianNB()
            naive_baye.fit(self.X_train, self.y_train)
            predict = naive_baye.predict(self.X_test)
            score = accuracy_score(self.y_test, predict) * 100
            return score
            
    # helper method
    def clean(self):
        dc = data_cleaner(self.test, self.train)
        dc.clean_gender()
        dc.clean_creditHistory()
        dc.clean_dependant()
        dc.clean_eduction()
        dc.clean_loadStatus()
        dc.clean_loanAmount()
        dc.clean_married()
        dc.clean_propertyArea()
        dc.clean_selfEmployed()
        
        self.train, self.test = dc.get_test_train()

    def get_train_test(self):
        return (self.train, self.test)
    def shape(self):
        return (self.train.shape, self.test.shape)
    
    def sns_graph(dataset: any):
        sns.countplot(dataset
                      )

