import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import StockDataExtraction as SDE

##loading the information for the model.
stock_info = SDE.load_stock_data('SNAP') #Get the stock for some given ticker. SNAP in this example.

#Setting matplotlib styles and rcparams.
plt.style.use(['dark_background', 'presentation'])
matplotlib.rcParams['lines.linewidth'] = 2
matplotlib.rcParams['lines.linestyle'] = '--'
mpl.rcParams['axes.prop_cycle'] = cycler(color=['r', 'g', 'b', 'y'])
plt.plot(data)  # first color is red

def visualize_stock(colname):
    plt.figure()
    plt.plot(stock_info.index, stock_info[colname])
    plt.xlabel("date")
    plt.ylabel("$ price")
    plt.title(colname + " dataplot")
    plt.show()
    
print('''Enter the stock parameter to visualize: 
          1. Open
          2. High
          3. Low
          4. Close
          5. Adj Close
          6. Volume
      ''')
column = input("Enter response as a String")
visualize_stock(column)
