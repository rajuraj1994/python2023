import pandas as pd 
import matplotlib.pyplot as plt

x=pd.read_csv('pandas/data/matches.csv')
print(x.to_string())

x.plot()
plt.show()


