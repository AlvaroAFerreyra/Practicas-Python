import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

data.drop(['open','close','high','low','volume'],axis=1,inplace=True)

data = data[::-1]

newTable = pd.DataFrame()

year = 0

for year in range(2005,2016):
	since = pd.Timestamp(year,1,1)

	until = pd.Timestamp(year,12,31)

	newTable = data[(data['timestamp'] >= since) & (data['timestamp'] <= until)].copy()
			
	newTable['difIntraDay'] = newTable.adjusted_close / newTable.adjusted_close.shift(1)

	newTable['yield'] = (newTable.difIntraDay.cumprod()-1)*100

	print(f"El rendimiento anual del año {year} fue:")
	print(newTable[-1:]['yield'])