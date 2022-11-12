import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_excel('AAPL.xlsx')
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)
data.drop(['high','low','volume','close'], axis=1, inplace=True)

serie = {}
años = ['2015','2016','2017','2018','2019']
fig, ax = plt.subplots(figsize=(10,5))

for año in años:
	serie[año] = data.loc[(data.index >= año) & (data.index < str(int(año)+1))].dropna().copy()
	serie[año]['gap'] = (serie[año]['open'] / serie[año]['adjusted_close'].shift()-1)*100
	serie[año]['intra'] = (serie[año]['adjusted_close'] / serie[año]['open']-1)*100
	print(serie[año]['gap'].resample('Y').mean().to_frame())
	print(serie[año]['intra'].resample('Y').mean().to_frame())
	ax.plot(serie[año]['gap'].resample('Y').mean().to_frame())
	ax.plot(serie[año]['intra'].resample('Y').mean().to_frame())
	ax.legend(años, loc="upper left")



plt.show()