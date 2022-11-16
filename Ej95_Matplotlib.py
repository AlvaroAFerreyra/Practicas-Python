import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import mplfinance as mpf

data = pd.read_excel("SPY.xlsx").sort_values("timestamp", ascending=True)
data.set_index("timestamp", inplace=True)

data['factor'] = data.adjusted_close/data.close

columnas = [data.open*data.factor, data.high*data.factor, data.low*data.factor, data.adjusted_close, data.volume]

dataAj = pd.concat(columnas, axis=1)

dataAj.columns = ['open', 'high', 'low', 'close', 'volume']

print(dataAj)