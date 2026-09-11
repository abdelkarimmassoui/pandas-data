import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = np.array(['eurusd', 'gbpusd','gold'])
y = np.array([1453,564,873])
plt.barh(x, y, color='green', height=0.1)
plt.title('Currency and Commodity Prices')
plt.xlabel('Price')
plt.ylabel('Currency/Commodity')
plt.show()
plt.savefig('chart.png')  # Save as image