import pandas as pd
import datetime as dt

data = pd.read_excel('AAPL.xlsx')

newTable = pd.DataFrame()

data.drop(['open','close','high','low','volume'],axis=1,inplace=True)

data = data.sort_values(by='timestamp',ascending=True)

data['rendimiento'] = data.adjusted_close.pct_change()+1

newTable['rendimiento'] = (((data.rendimiento.groupby([data.timestamp.dt.year, data.timestamp.dt.month]).prod())-1)*100).to_frame()

print(newTable.loc[newTable['rendimiento']>20])