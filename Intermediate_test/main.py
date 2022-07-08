from ui.index import header, data_io, data_opt
from util.index import loading, pretty_output
from lib.index import data
import os

# change look out directory to locate dataset
parents = "6-intermediate_test\data\dataset\\"
os.chdir(os.getcwd() + "\\" + parents)

loading("receving data...")
data = data(
   'test_Y3wMUE5_7gLdaTN.csv',
   'train_u6lujuX_CVtuZ9i.csv'
)

data.clean()

loading() # ... 
# clean data

#split data
data.split_train_test(.3)

# VISUAL 
# print header msg
print(header('Simple Load Prediction Model', data_io.data_file_msg()))

# preview data
train = data.train
print(train.head)

# print available options and pass the result to models available
opt_input = data_opt.model_types()
model_result = data.model(opt_input)
pretty_output(f"Accuracy for {opt_input}", model_result, "%")


