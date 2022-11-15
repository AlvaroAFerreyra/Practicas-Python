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

fig, ax0 = plt.subplots(figsize=(10,5))
ax0.set_ylabel('Intradiarios')
ax0.plot(maxIntra, color="grey")
ax0.plot(minIntra, color="green")
ax0.legend(['maxIntra','minIntra'], loc='upper left')
ax1 = ax0.twinx()
ax1.set_ylabel('Volatilidad')
ax1.plot(volatilidadMax, color="red", ls="--")
ax1.plot(volatilidadMin, color="blue", ls="--")
ax1.legend(['volatilidadMax','volatilidadMin'], loc='upper right')

plt.show()