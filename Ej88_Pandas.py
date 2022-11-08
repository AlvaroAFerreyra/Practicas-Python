import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("AAPL.xlsx")
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)

precios = {}
años = [['2014','2015','2016'],['2017','2018','2019']]

fig, ax = plt.subplots(nrows=len(años), ncols=len(años[0]), figsize=(10,5))

for fila in range(len(años)):
	for columna in range(len(años[0])):
		precios[años[fila][columna]] = data.adjusted_close.loc[(data.index >= años[fila][columna]) & (data.index < str(int(años[fila][columna])+1))]
		serie = precios[años[fila][columna]].reset_index(drop=True)
		ax[fila][columna].plot(serie)
		ax[fila][columna].legend([años[fila][columna]], loc='lower right')
		ax[fila][columna].set_xticks([])

plt.show()



