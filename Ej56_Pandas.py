import pandas as pd
import datetime as dt

data = pd.read_excel('AAPL.xlsx')

newTable = pd.DataFrame()

data.drop(['open','close','volume','high','low'],axis=1,inplace=True)

data = data.sort_values('timestamp',ascending=True)

data['rendimiento'] = data.adjusted_close.pct_change()+1

newTable = data.rendimiento.groupby(data.timestamp.dt.year).prod().to_frame()

newTable['rendimiento'] = (newTable['rendimiento']-1)*100

print(newTable.loc[newTable['rendimiento']<0])



