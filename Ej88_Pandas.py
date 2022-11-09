import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_excel("AAPL.xlsx")
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)
data['var'] = (data.adjusted_close.pct_change()+1)*100
data['acum'] = data['var'] + data['var'].shift()

variaciones = {}
años = ['2014','2015','2016','2017','2018','2019']

fig, ax = plt.subplots(figsize=(10,5))

for año in años:
	variaciones[año] = data['var'].loc[(data.index >= año) & (data.index < str(int(año)+1))]
	serie = variaciones[año].reset_index(drop=True)
	ax.plot(serie)
	ax.legend(años, loc='lower right')


plt.show()



