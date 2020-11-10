from pmdarima import auto_arima 
import statsmodels.api as sm
# Ignore harmless warnings 
import warnings 
warnings.filterwarnings("ignore") 
import pandas as pd
import numpy as np

def arima(df):

  print("Y()")
  '''
  stepwise_fit = auto_arima(df['Stock_Price'], start_p = 1, start_q = 1, 
                          max_p = 3, max_q = 3, m = 12, 
                          start_P = 0, seasonal = True, 
                          d = None, D = 1, trace = True, 
                          error_action ='ignore',   # we don't want to know if an order does not work 
                          suppress_warnings = True,  # we don't want convergence warnings 
                          stepwise = True)       
  print(stepwise_fit.summary())
  '''
  
  mod = sm.tsa.statespace.SARIMAX(df['Stock_Price'],
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)    

    
  result = mod.fit() 
  print(result.summary())
  print("FINISHED MODEL")
  #model_fit = model.fit()
  #predictions = model_fit.predict(start=len(y)+1, end=len(y)+1, dynamic=False)
  #yhat = predictions[0]
  #print(yhat)

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