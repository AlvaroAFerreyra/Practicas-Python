import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

data.drop(['open','close','high','low','volume'],axis=1,inplace=True)

data = data[::-1]

for i in range(len(data)):
	if data.loc[i, 'timestamp'] > '2007-12-31' and data.loc[i, 'timestamp'] < '2009-01-01':
		

print(data)