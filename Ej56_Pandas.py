import pandas as pd
import datetime as dt

data = pd.read_excel('AAPL.xlsx')

newTable = pd.DataFrame()

"""data.set_index('timestamp', inplace=True)"""

data.drop(['open','close','volume','high','low'],axis=1,inplace=True)

data = data.sort_values('timestamp',ascending=True)

data['rendimiento'] = data.adjusted_close.pct_change()*100

newTable = data.rendimiento.groupby(data.timestamp.dt.year).prod().to_frame()

print(newTable)

