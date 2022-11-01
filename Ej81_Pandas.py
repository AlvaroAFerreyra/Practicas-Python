import pandas as pd

data = pd.read_excel('AAPL.xlsx')
data = data.sort_values("timestamp", ascending=True)
data.set_index("timestamp", inplace=True)
data['price'] = data.adjusted_close
data['pctChange'] = data.adjusted_close.pct_change()*100
data['openGap'] = (data.open/data.close.shift(1)-1)*100
data['intraMov'] = (data.close/data.open-1)*100

newTable = data.drop(['open','high','low','close','volume','adjusted_close'], axis=1).dropna()
newTable.index.name = 'date'

print(newTable)