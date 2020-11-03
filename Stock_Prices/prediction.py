import pandas as pd
import datetime
from pytz import timezone

def prediction_ma(training):
    pred_ma=sum(training.iloc[-5:,1])/5
    return pred_ma
    

def main():
    data=pd.read_csv('Stock1.csv')
    data=pd.DataFrame(data,index=data.iloc[:,0])
    data=data.iloc[:,1:]
    #print(data)
    
    test=pd.DataFrame(data.iloc[:,4:6])
    
    test['DateTime'] = pd.to_datetime(test['DateTime'])
    
    now=test.iloc[-1,0]
    future = now+ datetime.timedelta(0,30) 
    
    test.loc[len(test)]=[future,0]
    
    
    training=test.iloc[:len(test)-1,]
    testing=test.iloc[len(test)-1:,]
    
    ma_pred=prediction_ma(training)
    
    
    #print("PREDICTION:", str(ma_pred))
    
    return ma_pred