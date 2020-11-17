import math
import numpy as np

from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Dense, LSTM

import pandas as pd
import pandas_datareader as reader

import matplotlib.pyplot as plt

from dataProcessing.preprocessing import preprocess_data

plt.style.use('fivethirtyeight')

# List of Companies to be analyzed
companies = ['AAPL', 'MSFT', 'AMD', 'INTC']
# Target company index
target = 0
# Sets the number of days the LSTM will use in the prediction
sample_size = 60

#target_quotes = reader.DataReader(companies[target], data_source='yahoo', start='2011-01-01')

X_normalized, y_normalized, y, y_scaler = preprocess_data(companies[target])

train_test_split = 0.8521

X_train = X_normalized[:int(len(X_normalized)*train_test_split)]
X_test = X_normalized[int(len(X_normalized)*train_test_split):]
y_train = y_normalized[:int(len(y_normalized)*train_test_split)]
y_test = y_normalized[int(len(y_normalized)*train_test_split):]

y_test_actual = y[int(len(y_normalized)*train_test_split):]

# Building the LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, batch_size=1, epochs=1)

# Get the models predicted price values
predictions = model.predict(X_test)
# The scaler expects the array to be a multidimensional array
predictions = np.concatenate((predictions, predictions), axis=1)
predictions = np.concatenate((predictions, predictions), axis=1)
# Remove the scalling on the model
predictions = y_scaler.inverse_transform(predictions)
predictions = predictions.T[0].T
predictions = np.reshape(predictions, (predictions.shape[0], 1))

# Get the root mean square error (RMSE)
rmse = np.sqrt(np.mean(((predictions.T[0] - y_test_actual.T[0]) ** 2)))

import csv

def csvEditor(fileName, data, type):
    with open(f'{fileName}', f'{type}', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


csvEditor("../data/" + companies[target]+ "lstmOutput.csv", predictions.T[0], 'w')
csvEditor("../data/" + companies[target]+ "actualOutput.csv", y_test_actual.T[0], 'w')
model.save('technical_model.h5')