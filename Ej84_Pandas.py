import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('SPY.xlsx')
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)

años = ['2014','2015','2016','2017','2018','2019']
precios = {}

for año in años:
	precios[año] = data.adjusted_close.loc[(data.index >= str(año)) & (data.index < str(int(año)+1))]
	precios[año] = precios[año].reset_index(drop=True)
	line = plt.plot(precios[año], lw=1)

plt.legend(años, loc='upper left')
plt.show()	