import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rd



#random 
n = np.array([12,72,99,9])
plt.pie(n,labels=['us30','eurusd','gbpusd','xauusd'],startangle=0,explode=(0,0.5,0,0),shadow=True)
plt.legend()
plt.show()