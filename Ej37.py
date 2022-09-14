import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

nuevaTabla = pd.DataFrame()

nuevaTabla['fecha'] = data.timestamp
nuevaTabla['volumen'] = data.volume
nuevaTabla['difVolume'] = data['volume'].diff(-1)

nuevaTabla.set_index('fecha', inplace=True)

print(nuevaTabla)