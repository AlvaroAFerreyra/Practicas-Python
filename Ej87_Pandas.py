import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('SPY.xlsx')
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)

numRuedas = int(input("Ingrese el número de ruedas: "))
años = ['2014','2015','2016','2017','2018','2019']
years = [[2014,2015,2016],[2017,2018,2019]]
precios = {}

for año in años:
	precios[año] = data.adjusted_close.loc[(data.index >= año) & (data.index < str(int(año)+1))]
	precios[año] = precios[año].reset_index(drop=True)

fig, ax = plt.subplots(nrows=len(years), ncols=len(years[0]), figsize=(10,5))

for fila in range(len(years)):
	for columna in range(len(years[0])):
		year = str(years[fila][columna])
		serie = precios[year].loc[0:numRuedas]
		ax[fila][columna].plot(serie)
		ax[fila][columna].legend([year], loc='lower right')

plt.show()		

