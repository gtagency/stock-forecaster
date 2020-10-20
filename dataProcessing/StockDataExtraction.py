import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import datetime
import dateutil

yf.pdr_override()

#get dates for today and ten years back
end = datetime.date.today()
start = end - dateutil.relativedelta.relativedelta(years=10)

#input stock name
ticker = input('Enter stock ticker:') 

allinfo = pdr.get_data_yahoo(ticker, start, end)
allinfo['Daily Volatility'] = 100*(allinfo['High']-allinfo['Low'])/allinfo['Low']
allinfo['Daily Change'] = 100*(allinfo['Adj Close']-allinfo['Open'])/allinfo['Open']

print(allinfo.head())
print(allinfo.tail())
#print(allinfo.columns)