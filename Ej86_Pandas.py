import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('SPY.xlsx')
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)

numRuedas = int(input("Ingrese el número de ruedas: "))
años = ['2014','2015','2016','2017','2018','2019']
precios = {}
fig, ax = plt.subplots(figsize=(10,5))
fig.suptitle('Cierres ajustados 2014-2019')

for año in años:
	precios[año] = (data.adjusted_close.loc[(data.index >= año) & (data.index < str(int(año)+1))]).head(numRuedas)
	precios[año] = precios[año].reset_index(drop=True)
	line = plt.plot(precios[año])

plt.legend(años, loc="lower right")
plt.show()


