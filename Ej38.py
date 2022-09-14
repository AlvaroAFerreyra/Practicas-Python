import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

nuevaTabla = pd.DataFrame()

nuevaTabla['fecha'] = data.timestamp
nuevaTabla['cierre'] = data.close
nuevaTabla['forward5'] = data.close.diff(5)

nuevaTabla.set_index('fecha', inplace=True)

print(nuevaTabla)