import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

data['max_intraDay'] = round(((data.high/data.open)*100)-100, 2)

data.drop(["open","high","low","close","adjusted_close",'volume'],axis=1,inplace=True)

baseOrdenada = (data.sort_values(by='max_intraDay', ascending=False)).head(10)

print(baseOrdenada)

baseOrdenada.to_excel('Ej34.xlsx',sheet_name="Ejercicio")
