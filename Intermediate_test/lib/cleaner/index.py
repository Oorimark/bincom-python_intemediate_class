from this import s
import pandas as pd
class data_cleaner():
    def __init__(self, test, train) -> None:
        self.test = test
        self.train = train
    
    def clean_gender(self):
        # clean gender: filling none value and subbing Male to 1 and Female 0
        self.train.Gender = self.train.Gender.fillna(self.train.Gender.mode())
        self.test.Gender = self.test.Gender.fillna(self.test.Gender.mode())

        sex = pd.get_dummies(self.train['Gender'] , drop_first = True )
        self.train.drop(['Gender'], axis = 1 , inplace =True)
        self.train = pd.concat([self.train , sex ] , axis = 1)

        sex = pd.get_dummies(self.test['Gender'] , drop_first = True )
        self.test.drop(['Gender'], axis = 1 , inplace =True)
        self.test = pd.concat([self.test , sex ] , axis = 1)
        
    def clean_dependant(self):
        # clean dependents and converting to int 1,2,3
        self.train.Dependents = self.train.Dependents.fillna("0")
        self.test.Dependents = self.test.Dependents.fillna("0")

        rpl = {'0':'0', '1':'1', '2':'2', '3+':'3'}

        self.train.Dependents = self.train.Dependents.replace(rpl).astype(int)
        self.test.Dependents = self.test.Dependents.replace(rpl).astype(int)

    def clean_creditHistory(self):
        self.train.Credit_History = self.train.Credit_History.fillna(self.train.Credit_History.mode()[0])
        self.test.Credit_History  = self.test.Credit_History.fillna(self.test.Credit_History.mode()[0])
        
    def clean_selfEmployed(self):
        self.train.Self_Employed = self.train.Self_Employed.fillna(self.train.Self_Employed.mode())
        self.test.Self_Employed = self.test.Self_Employed.fillna(self.test.Self_Employed.mode())

        self_Employed = pd.get_dummies(self.train['Self_Employed'] ,prefix = 'employed' ,drop_first = True )
        self.train.drop(['Self_Employed'], axis = 1 , inplace =True)
        self.train = pd.concat([self.train , self_Employed ] , axis = 1)

        self_Employed = pd.get_dummies(self.test['Self_Employed'] , prefix = 'employed' ,drop_first = True )
        self.test.drop(['Self_Employed'], axis = 1 , inplace =True)
        self.test = pd.concat([self.test , self_Employed ] , axis = 1)
        
    def clean_married(self):
        self.train.Married = self.train.Married.fillna(self.train.Married.mode())
        self.test.Married = self.test.Married.fillna(self.test.Married.mode())

        married = pd.get_dummies(self.train['Married'] , prefix = 'married',drop_first = True )
        self.train.drop(['Married'], axis = 1 , inplace =True)
        self.train = pd.concat([self.train , married ] , axis = 1)

        married = pd.get_dummies(self.test['Married'] , prefix = 'married', drop_first = True )
        self.test.drop(['Married'], axis = 1 , inplace =True)
        self.test = pd.concat([self.test , married ] , axis = 1)
        
    def clean_loanAmount(self):
        self.train.drop(['Loan_Amount_Term'], axis = 1 , inplace =True)
        self.test.drop(['Loan_Amount_Term'], axis = 1 , inplace =True)

        self.train.LoanAmount = self.train.LoanAmount.fillna(self.train.LoanAmount.mean()).astype(int)
        self.test.LoanAmount = self.test.LoanAmount.fillna(self.test.LoanAmount.mean()).astype(int)
        
    def clean_eduction(self):
        self.train['Education'] = self.train['Education'].map( {'Graduate': 0, 'Not Graduate': 1} ).astype(int)
        self.test['Education'] = self.test['Education'].map( {'Graduate': 0, 'Not Graduate': 1} ).astype(int)

    def clean_propertyArea(self):
        self.train['Property_Area'] = self.train['Property_Area'].map( {'Urban': 0, 'Semiurban': 1 ,'Rural': 2  } ).astype(int)

        self.test.Property_Area = self.test.Property_Area.fillna(self.test.Property_Area.mode())
        self.test['Property_Area'] = self.test['Property_Area'].map( {'Urban': 0, 'Semiurban': 1 ,'Rural': 2  } ).astype(int)

    def clean_loadStatus(self):
        self.train['Loan_Status'] = self.train['Loan_Status'].map( {'N': 0, 'Y': 1 } ).astype(int)
        
    # Helper functions
    def get_test_train(self):
        return (self.train, self.test)