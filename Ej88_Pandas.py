import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("AAPL.xlsx")
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)

años = [['2014','2015','2016'],['2017','2018','2019']]

for fila in len(años):
	for columna in len(años[0]):
		ax[fila][columna] = data.adjusted_close.loc([data.index == años[fila][columna]])




