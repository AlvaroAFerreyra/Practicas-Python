import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_excel("tablaBollinger.xlsx")

data.set_index("timestamp", inplace=True)

data = data[data.index < "2009-01-01"]

resultados = []

dataFiltrada = data.loc[data.adjusted_close > data.supBollinger]

for i in range(21):

	data['precioForward'] = data.adjusted_close.shift(-i)

	data['varForward'] = (data.precioForward / data.adjusted_close -1)*100

	dataFiltrada = data.loc[data.adjusted_close > data.supBollinger]

	resultados.append(dataFiltrada.varForward.mean()/(i+1))

grafico = pd.DataFrame(resultados)

grafico.columns = ['resultados']
print(grafico)
fig, ax=plt.subplots()
ax.bar(grafico.index, grafico.resultados)


plt.show()