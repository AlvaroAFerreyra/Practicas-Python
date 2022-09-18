import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

data.drop(['volume','high','low'], axis=1, inplace=True)

data['gap'] = data.open/data.close.shift(-1)

data['varPorcAdjClose'] = round((data.adjusted_close.pct_change(5)-1), 2)

print(data.dropna())

