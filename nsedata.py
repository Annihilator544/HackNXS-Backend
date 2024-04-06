from datetime import date
from nsepy import get_history
sbin = get_history(symbol='SBIN',
                   start=date(2015,1,1),
                   end=date(2015,1,10))
print(sbin)