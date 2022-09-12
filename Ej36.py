import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

baseFiltrada = data[(data['volume']>150000000) | (data['volume']<1000000)]

print(baseFiltrada[['timestamp','volume']])