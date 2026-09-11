import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = np.array(['eurusd', 'gbpusd','gold'])
y = np.array([1453,564,873])
plt.bar(x, y)
plt.show()
plt.savefig('chart.png')  # Save as image