import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_excel("AAPL.xlsx")
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)

variaciones = {}
años = ['2014','2015','2016','2017','2018','2019']

fig, ax = plt.subplots(figsize=(10,5))

for año in años:
	variaciones[año] = data.loc[(data.index >= año) & (data.index < str(int(año)+1))].copy()
	variaciones[año]['pct_ch'] = variaciones[año]['adjusted_close'].pct_change()+1
	variaciones[año]['rendimiento'] = variaciones[año]['pct_ch'].cumprod()*100
	variaciones[año].dropna(inplace=True)
	variaciones[año] = variaciones[año].reset_index(drop=True)
	ax.plot(variaciones[año]['rendimiento'])
	ax.legend(años, loc='upper left')


plt.show()



