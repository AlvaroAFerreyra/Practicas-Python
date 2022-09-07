import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

baseFiltrada = data[data['timestamp']>"2008-05-15" & ]