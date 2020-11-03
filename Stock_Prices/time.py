from datetime import datetime
from pytz import timezone
 
est=timezone('EST')
d= datetime.now(est)
time=str(d.time())[:-7]
final=str(d.date()) + " "+ time
final1=datetime.strptime(final, '%Y-%m-%d %H:%M:%S')
print(final1)
