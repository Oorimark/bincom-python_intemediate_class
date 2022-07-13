import pandas as pd

class cleaner:
    data: any 

    def __init__(self, data: any) -> None:
        self.data = data
        
    def isnull_avg(self, set: list):
        for i in set:
            cleaned_i = self.data[i].fillna(self.data[i].mean())
            drop_i = self.data.drop([i])
            self.data = pd.concat([drop_i, cleaned_i], axis = 1)
    
    def get_cleaned_data(self):
        return self.data