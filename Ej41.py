import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

data.drop(['adjusted_close','volume','high','low'], axis=1, inplace=True)

data['intraDay'] = abs(data.close/data.open-1)*100

contador = data.intraDay[(data.intraDay > 3)].count()

print(data)

print(contador)