import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_excel("AAPL.xlsx")
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)
data['intraDay'] = (data.close / data.open-1)*100

maxIntra = data.intraDay.groupby(data.index.year).max()
minIntra = data.intraDay.groupby(data.index.year).min()
volatilidad = data.adjusted_close.groupby(data.index.year).std()*250**0.5

fig, ax = plt.subplots(ncols=2, figsize=(10,5))
ax[0].plot(maxIntra)
ax[0].plot(minIntra)
ax[0].legend(['maxIntra','minIntra'], loc='upper left')
ax[1].plot(volatilidad)
ax[1].legend(['volatilidad'], loc='upper right')

plt.show()
