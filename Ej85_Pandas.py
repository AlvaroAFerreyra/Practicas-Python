import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('SPY.xlsx')
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)

años = ['2014','2015','2016','2017','2018','2019']
precios = {}
fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(10,5))
fig.suptitle('Cierres ajustados 2014-2019')

for año in años:
	precios[año] = (data.adjusted_close.loc[(data.index >= año) & (data.index < str(int(año)+1))]).head(250)
	precios[año] = precios[año].reset_index(drop=True)

for i in range(2):
	for a in range(3):
			for año in precios:
				ax[i][a].plot(precios[año], lw=1)
				ax[i][a].legend([año], loc = 'lower right')



plt.show()	