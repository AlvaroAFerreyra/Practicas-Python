import pandas as pd
import datetime as dt

data = pd.read_excel("AAPL_INTRA.xlsx")

newTable = pd.DataFrame()

data.drop(['high','low','open','close','adjusted_close'], axis=1, inplace=True)

data.set_index('datetime', inplace=True)

data = data.sort_values('datetime',ascending=True)

newTable['volTotal'] = data['volume'].resample('W').sum().to_frame()

print(newTable)