import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('SPY.xlsx')
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)

años = []
precios = {}

desde = input("Ingrese el año desde el que quiere comparar: ")
hasta = input("Ingrese el año hasta el que quiere comparar: ")

plt.style.use('fivethirtyeight')

for i in range(int(desde), int(hasta)+1):
	años.append(i)

for año in años:
	precios[año] = data.adjusted_close.loc[(data.index >= str(año)) & (data.index < str(año+1))]
	precios[año] = precios[año].reset_index(drop=True)
	line = plt.plot(precios[año], lw=1)

plt.legend(años, loc='upper left')
plt.show()	

