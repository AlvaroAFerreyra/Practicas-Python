import pandas as pd
import datetime as dt

newTable = pd.DataFrame()

data = pd.read_excel("AAPL_INTRA.xlsx")

data.drop('adjusted_close', axis=1, inplace=True)

data.set_index('datetime', inplace=True)

data = data.sort_values('datetime', ascending=True)

data['precioMedio'] = (data.open + data.close + data.high + data.low) / 4

data['volumenNegociadoEnMillones'] = data.precioMedio * data.volume / 1000000

newTable['volumenNegociadoEnMillones'] = data.volumenNegociadoEnMillones.resample('D').sum().to_frame()

newTable = newTable.loc[newTable['volumenNegociadoEnMillones'] > 0]

print(newTable)