import matplotlib.pyplot as plt
import numpy as np

company = 'AAPL'
lstm_data = np.genfromtxt('../data/' + company + 'lstmOutput.csv', delimiter=',')
actual_data = np.genfromtxt('../data/' + company + 'actualOutput.csv', delimiter=',')

xrange = range(0, len(lstm_data))
plt.plot(xrange, lstm_data, label='LSTM predicted')
plt.plot(xrange, actual_data, label='Actual stock prices')
plt.legend(loc="upper left")
plt.xlabel("Days")
plt.ylabel("Price")
plt.show()