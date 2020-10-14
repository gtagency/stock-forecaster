import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import datetime

yf.pdr_override()

start = datetime.date(2018,1,1)
end = datetime.date.today()

ticker = input('Enter stock ticker:') 

allinfo = pdr.get_data_yahoo(ticker, start, end)
allinfo['Daily Volatility'] = 100*(allinfo['High']-allinfo['Low'])/allinfo['Low']
allinfo['Daily Change'] = 100*(allinfo['Adj Close']-allinfo['Open'])/allinfo['Open']

print(allinfo.head())
print(allinfo.tail())