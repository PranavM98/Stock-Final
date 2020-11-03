from datetime import datetime

def date_time_format(est):
    d= datetime.now(est)
    time=str(d.time())[:-7]
    final=str(d.date()) + " "+ time
    final1=datetime.strptime(final, '%Y-%m-%d %H:%M:%S')
    return final1

def moving_average(df):
    ma=0
    ma=sum(df.iloc[-5:,5])/5
    return ma
    
def calculate_price_diff(price,p_diff):
    p_diff.append(price)
    if len(p_diff)==1:
        return 0
    else:
        return p_diff[len(p_diff)-1]-p_diff[len(p_diff)-2]

    
def index_price_difference(ind_price,ind):
    ind.append(ind_price)

    if len(ind)==1:
        return 0
        
    else:
        return ind[len(ind)-1]-ind[len(ind)-2]