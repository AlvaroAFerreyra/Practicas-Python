import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

baseFilter = data[(data['timestamp']>"2017-12-31") & (data['timestamp']<"2019-01-01")]

baseFilter['min_intraDay'] = round(((baseFilter.low/baseFilter.open)*100)-100, 2)

baseOrder = baseFilter.sort_values(by='min_intraDay',ascending=True)

print(baseOrder.head(5))