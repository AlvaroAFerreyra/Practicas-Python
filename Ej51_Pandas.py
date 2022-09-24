import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

data.drop(['high','low','volume','open','close'],axis=1,inplace=True)

for i in range(len(data)):
	data.loc[i,'maxHistorico'] = data.loc[0:i,'adjusted_close'].max()

print(data)