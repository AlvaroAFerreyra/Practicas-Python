import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

data.drop(['volume','high','low'], axis=1, inplace=True)

data['gap'] = (data.open/data.close.shift(-1)-1)*100

data['varPorcAdjClose'] = ((data.adjusted_close.shift(5)/data.adjusted_close)-1)*100



newTable = pd.DataFrame()

for i in data['gap']:
	if i > 1:
			newTable['fecha'] = data.timestamp
			newTable['apertura'] = data.open
			newTable['cierre'] = data.close
			newTable['gap'] = data.gap
	

print(newTable)		