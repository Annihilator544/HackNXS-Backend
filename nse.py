
import nsepy as ns
from datetime import date
import time
import pandas as pd

nse_list = ['Infosys']


stocks = []
try:
 for i, elem in enumerate(nse_list):
  print(i,elem)
  stock = ns.get_history(symbol=elem,
                   start=date.today,
                   end=date.today)
  
  if stock is not None:
   stocks.append(stock)
  
  time.sleep(10)
 stocks = pd.concat(stocks)
 stocks.to_csv(r'50_nifty_stock_data_test_tut1.csv')  
 

except:
 stocks = pd.concat(stocks)
 stocks.to_csv(r'50_nifty_stock_data_test_tut1.csv')




