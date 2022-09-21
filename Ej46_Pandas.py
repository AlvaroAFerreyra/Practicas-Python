import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

data.drop(['adjusted_close'], axis=1, inplace=True)

data = data[::-1]

data["precioMedio"] = (data.open+data.close+data.low+data.high)/4

data['volEnMillones'] = (data.precioMedio*data.volume)/1000000

data['mobileMedia_20'] = data.volEnMillones.rolling(20).mean()

print(data)

