import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


data = pd.read_excel("tablaBollinger.xlsx")

data.set_index("timestamp", inplace=True)

data = data[data.index < "2009-01-01"]

resultados = []

dataFiltrada = data.loc[data.adjusted_close > data.supBollinger]

for i in range(21):

	data['precioForward'] = data.adjusted_close.shift(-i)

	data['varForward'] = (data.precioForward / data.adjusted_close -1)*100

	dataFiltrada = data.loc[data.adjusted_close > data.supBollinger]

	resultados.append(dataFiltrada.varForward.mean())

grafico = pd.DataFrame(resultados)

plt.bar(grafico)

plt.show()