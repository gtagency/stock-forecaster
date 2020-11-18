import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import datetime
import dateutil
import os.path
import ta

def load_stock_data(tickername):
    #To get the data in a pandas dataframe
    yf.pdr_override()

    #get dates for today and ten years back
    end = datetime.date.today()
    start = end - dateutil.relativedelta.relativedelta(years=10)

    #input stock name
    ticker = tickername
    
    #Pull stock info from CSV if CSV exists
    if os.path.isfile(ticker + '.csv') :
        allinfo = pd.read_csv (ticker + '.csv')
        print(allinfo.head())
        print(allinfo.tail())

    #get stock info for past 10 years and calculate daily volatility, change, moving average, and RSI.
    else:
        try: 
            allinfo = pdr.get_data_yahoo(ticker, start, end)
        except:
            print("Enter a proper ticker!")
        allinfo['Daily Volatility'] = 100*(allinfo['High']-allinfo['Low'])/allinfo['Low']
        allinfo['Daily Change'] = 100*(allinfo['Adj Close']-allinfo['Open'])/allinfo['Open']
        indicator_bb = ta.volatility.BollingerBands(close=allinfo["Adj Close"], n=20, ndev=2)
        indicator_RSI = ta.momentum.RSIIndicator(close=allinfo["Close"], n=14, fillna =False)
        allinfo['BB_Moving Avg'] = indicator_bb.bollinger_mavg()
        allinfo['RSI'] = indicator_RSI.rsi()
        
        #Method to remove NaN values
        #df = ta.utils.dropna(df)
        
        #print(type(allinfo))
        #print(allinfo.head())
        #print(allinfo.tail())
        #print(allinfo.columns)

        # creates a csv file to hold data
        allinfo.to_csv(ticker + '.csv')

#sample input
load_stock_data('aapl')


