import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('SPY.xlsx')
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)

años=[]
cierres=[]
l=0

desde = input("Ingrese el año desde el que quiere comparar: ")
hasta = input("Ingrese el año hasta el que quiere comparar: ")

añoInic = desde

for i in range(int(desde), int(hasta)+1):
	var = data.adjusted_close.loc[data.index == i]
	var = var.reset_index(drop=True)
	años.append(i)
	cierres.append(var)

fig, ax = plt.subplots(figsize=(10,7))
for a in años:
	a = plt.plot(cierres[l])
	l=l+1

plt.show()	

