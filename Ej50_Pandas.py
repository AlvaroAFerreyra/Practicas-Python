import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

data.drop(['high','low','volume','open','close'],axis=1,inplace=True)

data['maxHistorico'] = data.adjusted_close.cummax()

print(data)