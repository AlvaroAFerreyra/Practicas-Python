import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("AAPL.xlsx")
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)

precios = {}
años = ['2014','2015','2016','2017','2018','2019']

fig, ax = plt.subplots(figsize=(10,5))

for año in años:
	precios[año] = data.adjusted_close.loc[(data.index >= año) & (data.index < str(int(año)+1))]
	serie = precios[año].reset_index(drop=True)
	ax.plot(serie)
	ax.legend(años, loc='lower right')


plt.show()



