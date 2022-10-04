import pandas as pd
import datetime as dt

newTable = pd.DataFrame()

data = pd.read_excel("AAPL_INTRA.xlsx")

data.drop(['adjusted_close'],axis=1, inplace=True)

data.set_index('datetime', inplace=True)

data = data.sort_values('datetime', ascending=True)

data['precioMedio'] = (data.open + data.close + data.high + data.low) / 4

newTable['volumenTotal'] = data['volume'].resample('D').sum().to_frame()

newTable['precioMedio'] = data['precioMedio'].resample('D').mean().to_frame()

newTable['volumenNegociadoEnMillones'] = newTable.volumenTotal * newTable.precioMedio / 1000000

print(newTable.dropna())