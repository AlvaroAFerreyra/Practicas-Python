import pandas as pd
import datetime as dt

newTable = pd.DataFrame()

data = pd.read_excel("AAPL_INTRA.xlsx")

data.drop(['high','low','open','close','volume'],axis=1,inplace=True)

data.set_index('datetime',inplace=True)

data = data.sort_values('datetime',ascending=True)

newTable['precioMedio'] = data['adjusted_close'].resample('D').mean().to_frame()


print(newTable.dropna())