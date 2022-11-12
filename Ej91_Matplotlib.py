import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_excel("AAPL.xlsx")
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)
data['intraDay'] = (data.close / data.open-1)*100
data['volatilidad'] = (data.adjusted_close/data.adjusted_close.shift(1)-1).rolling(250).std()*250**0.5*100

maxIntra = data.intraDay.groupby(data.index.year).max()
minIntra = data.intraDay.groupby(data.index.year).min()
volatilidadMax = data.volatilidad.groupby(data.index.year).max()
volatilidadMin = data.volatilidad.groupby(data.index.year).min()

fig, ax = plt.subplots(ncols=2, figsize=(10,5))
ax[0].plot(maxIntra)
ax[0].plot(minIntra)
ax[0].legend(['maxIntra','minIntra'], loc='upper left')
ax[1].plot(volatilidadMax)
ax[1].plot(volatilidadMin)
ax[1].legend(['volatilidadMax','volatilidadMin'], loc='upper right')

plt.show()
