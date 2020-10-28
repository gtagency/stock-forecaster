import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import datetime
import dateutil
def load_stock_data(tickername):
    #To get the data in a pandas dataframe
    yf.pdr_override()

    #get dates for today and ten years back
    end = datetime.date.today()
    start = end - dateutil.relativedelta.relativedelta(years=10)

    #input stock name
    ticker = tickername

    #get stock info for past 10 years and calculate daily volatility and change.
    try: 
        allinfo = pdr.get_data_yahoo(ticker, start, end)
    except:
        print("Enter a proper ticker!")
    allinfo['Daily Volatility'] = 100*(allinfo['High']-allinfo['Low'])/allinfo['Low']
    allinfo['Daily Change'] = 100*(allinfo['Adj Close']-allinfo['Open'])/allinfo['Open']
    #print(type(allinfo))
    #print(allinfo.head())
    #print(allinfo.tail())
    #print(allinfo.columns)
    return allinfo
