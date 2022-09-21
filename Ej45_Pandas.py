import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

data.drop(['volume','high','low'], axis=1, inplace=True)

data['gap'] = (data.open/data.close.shift(-1)-1)*100

data['varPorcAdjClose'] = ((data.adjusted_close.shift(5)/data.adjusted_close)-1)*100

filtro1 = data[data['gap'] > 1]

filtro2 = filtro1[filtro1['varPorcAdjClose'] > 0]

print((len(filtro2)/len(data))*100)