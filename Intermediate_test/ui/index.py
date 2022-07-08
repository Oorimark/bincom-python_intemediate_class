def header(purpose, other_msg) -> str:
    hero_msg = "============= MARK'S INTEMEDIATE TEST ============ "
    msg = f"Hey, I am Jojo I'll help you with {purpose}, let's get started!"
    line = "=" * len(hero_msg)
    return f'\n{hero_msg} \n {msg} \n{other_msg} \n{line}'

# input-output
class data_io:
    def __init__(self) -> None:
        pass

    @staticmethod
    def input():
        return input("Enter search: ")
    @staticmethod 
    def data_file_msg():
        return "NB: This dataset used was from: https://www.kaggle.com/altruistdelhite04/loan-prediction-problem-dataset" 

# this class communicates with the machine model
class data_algo:
    ...

# options for the user
class data_opt:
    
    def model_types() -> str:
        header = "\nThe model available are:"
        ln_1 =  "Random Forest Classifier: type 1"
        ln_2 = "Navie Bayes Model: type 2"
        format = f"{header} \n{ln_1} \n{ln_2}"
        print(format)
        return input("Enter option: ")
        
    @staticmethod
    def graph():
        ...