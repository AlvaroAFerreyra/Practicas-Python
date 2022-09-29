import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

data.drop(['open','close','high','low','volume'],axis=1,inplace=True)

data = data[::-1]

newTable = pd.DataFrame()

newTable = data[(data['timestamp'] > '2007-12-31') & (data['timestamp'] < '2009-01-01')]
		
newTable['difIntraDay'] = newTable.adjusted_close / newTable.adjusted_close.shift(1)

newTable['yield'] = (newTable.difIntraDay.cumprod()-1)*100

print(newTable[-1:]['yield'])