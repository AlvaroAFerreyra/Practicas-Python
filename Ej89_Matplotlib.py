import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_excel("AAPL.xlsx")
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)

data['mm50'] = data.adjusted_close.rolling(50).mean()
data['mm200'] = data.adjusted_close.rolling(200).mean()

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(data.mm50)
ax.plot(data.mm200)
ax.legend(['mm50','mm200'], loc='upper left')
ax = plt.gca()
ax.set_yscale('log')
ent = data.mm50 > data.mm200
plt.fill_between(data.index, data.adjusted_close.max(), where=ent, color="yellow")
plt.show()