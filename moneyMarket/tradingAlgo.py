import pandas as pd
import numpy as np

company = 'AAPL'
lstm_data = np.genfromtxt('../data/' + company + 'lstmOutput.csv', delimiter=',')
actual_data = np.genfromtxt('../data/' + company + 'actualOutput.csv', delimiter=',')

buys = []
sells = []
thresh = 0.1

x = 1
for i in range(len(lstm_data[0:-1])):
    # normalised_price_today = ohlcv[-1][0]
    # normalised_price_today = np.array([[normalised_price_today]])
    price_today = actual_data[i]
    predicted_price_tomorrow = lstm_data[i+1]
    delta = predicted_price_tomorrow - price_today
    if delta > thresh:
        buys.append((x, price_today, delta))
    elif delta < -thresh:
        sells.append((x, price_today, delta))
    x += 1
print(f"buys: {len(buys)}")
print(f"sells: {len(sells)}")

def compute_earnings(buys_, sells_):
    purchase_amt = 10
    stock = 0
    balance = 0
    while len(buys_) > 0 and len(sells_) > 0:
        if buys_[0][0] < sells_[0][0]:
            # time to buy $10 worth of stock
            delta = buys_[0][2]
            balance -= purchase_amt * (10*delta)
            stock += (purchase_amt * (10*delta)) / buys_[0][1]
            buys_.pop(0)
        else:
            # time to sell all of our stock
            balance += stock * sells_[0][1]
            stock = 0
            sells_.pop(0)
    print(f"earnings: ${balance}")

compute_earnings([b for b in buys], [s for s in sells])