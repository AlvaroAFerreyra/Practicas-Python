import pandas as pd
import datetime as dt

newTable = pd.DataFrame()

data = pd.read_excel("AAPL_INTRA.xlsx")

data.drop(['volume','close'], axis=1, inplace=True)

data.set_index('datetime', inplace=True)

data = data.sort_values('datetime', ascending=True)

data['medio'] = (data.open + data.adjusted_close + data.low + data.high) / 4

newTable['minimo'] = data.low.resample('D').min().to_frame()

newTable['maximo'] = data.high.resample('D').max().to_frame()

newTable['medio'] = data.medio.resample('D').mean().to_frame()

print(newTable.dropna())