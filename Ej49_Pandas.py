import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

fast = 10
slow = 20

data = data[::-1]

data.drop(['open','close','high','low','volume'], axis=1, inplace=True)

data['mediLenta'] = data.adjusted_close.ewm(span=slow, adjust=False).mean()

data['mediRapida'] = data.adjusted_close.ewm(span=fast, adjust=False).mean()

data['cruce'] = (data.mediRapida/data.mediLenta-1)*100

print(data.round(4))
