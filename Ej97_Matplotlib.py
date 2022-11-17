import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import mplfinance as mpf

adr = str(input("Inserte el ADR buscado: ")).upper()
año = str(input("Inserte el año buscado: "))

data = pd.read_excel(adr+".xlsx")
data = data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)
data = data.loc[(data.index >= ('01-01-'+año)) & (data.index < ('01-04-'+str(int(año)+1)))]

data['factor'] = data.adjusted_close / data.close

columnas = [data.open*data.factor, data.high*data.factor, data.low*data.factor, data.adjusted_close, data.volume]

dataAj = pd.concat(columnas, axis=1)

dataAj.columns = ['open', 'high', 'low', 'close', 'volume']

mpf.plot(dataAj, type='candle', figratio=(14,5), volume=True, style='yahoo')