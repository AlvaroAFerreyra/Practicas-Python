import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

data.drop(['volume','high','low'], axis=1, inplace=True)

data['gap'] = (data.open/data.close.shift(-1)-1)*100

data['varPorcAdjClose'] = ((data.adjusted_close.shift(5)/data.adjusted_close)-1)*100

filtro = data[data['gap'] > 1]

print(filtro.isnull().sum())

