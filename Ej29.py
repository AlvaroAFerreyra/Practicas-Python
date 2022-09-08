import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

baseDateIndex = data.set_index('timestamp')

baseFiltrada = data[(data['timestamp']>"2008-05-15") & (data['timestamp']<"2011-08-20")]

print(baseFiltrada)

print(len(baseFiltrada))