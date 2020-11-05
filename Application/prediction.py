'''
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import pandas as pd
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
#import numpy as np
from keras.layers import Dropout

def lstm(data):

    scaler = MinMaxScaler(feature_range = (0, 1))

    data_scaled = scaler.fit_transform(data.iloc[:,6:7])
    
    features_set = []
    labels = []
    for i in range(40, 400):
      features_set.append(data_scaled[i-40:i-1, 0])
      labels.append(data_scaled[i, 0])
      
    features_set, labels = np.array(features_set), np.array(labels)
    features_set = np.reshape(features_set, (features_set.shape[0], features_set.shape[1], 1))
    
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(features_set.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))

    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))

    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    
    model.add(Dense(units = 1))
    model.compile(optimizer = 'adam', loss = 'mean_squared_error')
    model.fit(features_set, labels, epochs = 10, batch_size = 32)
    return True
    #predictions = model.predict(features_set)
    
    #labels= np.reshape(labels, (-1, 1))
    #predictions_in = scaler.inverse_transform(predictions)
    #labels_in = scaler.inverse_transform(labels)
    '''