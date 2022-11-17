import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import mplfinance as mpf

adr = input("Inserte el ADR buscado: ").upper()
año = int(input("Inserte el año buscado: "))
trimestre = int(input("Inserte el trimestre buscado: "))

if trimestre == 1:
	principio = dt.datetime(año,1,1)
	fin = dt.datetime(año,4,1)
elif trimestre == 2:
	principio = dt.datetime(año,4,1)
	fin = dt.datetime(año,7,1)
elif trimestre == 3:
	principio = dt.datetime(año,7,1)
	fin = dt.datetime(año,10,1)
elif trimestre == 4:
	principio = dt.datetime(año,10,1)
	fin = dt.datetime(año+1,1,1)	
else: print("Q fuera de rango")	



data = pd.read_excel(adr+".xlsx")
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)
data = data.loc[(data.index >= principio) & (data.index < fin)]

data['factor'] = data.adjusted_close / data.close

columnas = [data.open*data.factor, data.high*data.factor, data.low*data.factor, data.adjusted_close, data.volume]

dataAj = pd.concat(columnas, axis=1)

dataAj.columns = ['open', 'high', 'low', 'close', 'volume']

mpf.plot(dataAj, type='candle', figratio=(14,5), volume=True, style='yahoo')