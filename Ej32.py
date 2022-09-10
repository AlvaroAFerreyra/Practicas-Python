import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

baseFilter = data[(data['timestamp']>"2017-12-31") & (data['timestamp']<"2019-01-01")]

baseFilter['max_intraDay'] = (((baseFilter.high/baseFilter.open)*100)-100)

baseOrder = baseFilter.sort_values(by='max_intraDay',ascending=False)

print(baseOrder.head(5))