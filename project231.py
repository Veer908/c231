import pandas as pd 
from keras.model import Sequential
from keras.layers import Dense 

dataset = pd.read_csv(r'books.csv',error_bad_lines=False)

x = dataset.iloc[:, [4, 11]].values
y = dataset.iloc[:, 3].values

model = Sequential()
model.add(Dense(number of neurons, input_dim=8, activation='relu'))
model.add(Dense(number of neurons, activation='relu'))
model.add(Dense(number of neurons, activation='relu'))
model.add(Dense(number of neurons, activation='sigmoid'))

model.summary() 