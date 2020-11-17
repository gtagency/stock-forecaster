import pandas as pd
import numpy as np
from sklearn import preprocessing

def preprocess_data(ticker):
    df = pd.read_csv('../data/'+ticker+'.csv')
    df = df.drop('Date', axis=1)

    data = df.values
    num_of_days = 50

    #create minmaxscaler object for data processing/normalizing
    scaler = preprocessing.MinMaxScaler()

    #fit scaler to normalize data
    normalized_data = scaler.fit_transform(data)

    #separate data into sections of 50 days
    X_normalized = np.array([normalized_data[i:i+num_of_days].copy() for i in range(len(normalized_data)-num_of_days)])
    #get the opening price of 51st day for each 50 days for normalized prices
    y_normalized = np.array([normalized_data[i+num_of_days][0].copy() for i in range(len(normalized_data)- num_of_days)])
    y_normalized = np.reshape(y_normalized, (y_normalized.size, 1))

    #get normal opening price for 51st day
    y = np.array([data[i+num_of_days][0].copy() for i in range(len(data)- num_of_days)])
    y = np.reshape(y, (y.size, 1))

    #y normalizer needed to get values back to normal
    y_scaler = preprocessing.MinMaxScaler()
    y_scaler.fit(y)
    return X_normalized, y_normalized, y, y_scaler
