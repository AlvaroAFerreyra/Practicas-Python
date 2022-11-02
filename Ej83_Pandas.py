import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('SPY.xlsx')
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)

años=[]

desde = input("Ingrese el año desde el que quiere comparar: ")
hasta = input("Ingrese el año hasta el que quiere comparar: ")

for i in range(int(desde), int(hasta)+1):
	años.append(i)

print(años)