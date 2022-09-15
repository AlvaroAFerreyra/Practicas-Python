import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

newTable = pd.DataFrame()

newTable['fecha'] = data.timestamp
newTable['apertura'] = data.open
newTable['cierre'] = data.close
newTable['movIntraDay'] = ((data.close/data.open)-1)*100
newTable['movIntraDayPas'] = newTable.movIntraDay.shift(-1)
newTable['variacion'] = abs(newTable.movIntraDay) > abs(newTable.movIntraDayPas)

newTable.set_index('fecha', inplace=True)

print(newTable)