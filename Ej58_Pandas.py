import pandas as pd
import datetime as dt

newTable = pd.DataFrame()

data = pd.read_excel("AAPL.xlsx")

data = data.sort_values('timestamp',ascending=True)

data.drop(['high','low','open','close','volume'],axis=1,inplace=True)

data['rendimiento'] = data.adjusted_close.pct_change()+1

newTable['rendimiento'] = ((data.rendimiento.groupby([data.timestamp.dt.year, data.timestamp.dt.month]).prod()-1)*100).to_frame()

newTable.index.names = ["Año","Mes"]

newTable = newTable.sort_values('rendimiento',ascending=False)

print(newTable.head(10))