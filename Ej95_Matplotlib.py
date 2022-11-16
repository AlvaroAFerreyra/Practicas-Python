import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import mplfinance as mpf

data = pd.read_excel("SPY.xlsx").sort_values("timestamp", ascending=True)
data.set_index("timestamp", inplace=True)

data['factor'] = data.adjusted_close/data.close

columnas = [data.open*data.factor, data.high*data.factor, data.low*data.factor, data.adjusted_close, data.volume]

dataAj = pd.concat(columnas, axis=1)

dataAj.columns = [['open', 'high', 'low', 'close', 'volume']]

dataAj['sma20'] = dataAj.close.rolling(20).mean()
dataAj['std20'] = dataAj.close.rolling(20).std()
dataAj['bSup'] = dataAj.sma20 + 2*dataAj.std20
dataAj['bInf'] = dataAj.sma20 - 2*dataAj.std20

dataAj.dropna(inplace=True)

print(dataAj)

"""indicadores = dataAj['bolSup','sma20','bolInf']
agregados = mpf.make_addplots(indicadores)
mpf.plot(dataAj, volume=True, type='candle', figratio=(14,5), style='starsands tripes', addplot=agregados)"""

