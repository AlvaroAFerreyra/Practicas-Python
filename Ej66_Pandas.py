import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


bollinger = pd.read_excel("tablaBollinger.xlsx")

tablaFiltrada = bollinger[(bollinger.adjusted_close > bollinger.supBollinger) | (bollinger.adjusted_close < bollinger.lowBollinger)]

tablaFiltrada.set_index('timestamp', inplace=True)

conteo = tablaFiltrada.adjusted_close.groupby(tablaFiltrada.index.year)

conteo = conteo.count().to_frame()

fig, ax=plt.subplots()
ax.bar(conteo.index, conteo.adjusted_close)
plt.show() 
