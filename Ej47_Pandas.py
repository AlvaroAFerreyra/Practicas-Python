import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

data = data[::-1]

newTable = pd.DataFrame()

newTable['fecha'] = data.timestamp

newTable['cierreAjustado'] = data.adjusted_close

newTable['mediaMovil_50'] = data.adjusted_close.rolling(50).mean()

newTable['mediaMovil_200'] = data.adjusted_close.rolling(200).mean()

newTable['varForward_20'] = (data.adjusted_close.shift(-20)/data.adjusted_close-1)*100

print(newTable.dropna())