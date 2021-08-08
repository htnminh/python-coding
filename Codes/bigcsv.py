import pandas as pd
import matplotlib.pyplot as plt

path = r"C:\Users\Administrator\Desktop\gsquarterlySeptember20.csv"

data = pd.read_csv(path, low_memory=False)
data = data.set_index('time_ref')

data['value'].hist(bins=5)
plt.show()