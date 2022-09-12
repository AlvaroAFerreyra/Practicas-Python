import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

vol = list(data['volume'])

volHistMed = sum(vol)/len(vol)

data['varIntraDay'] = round((data.close/data.open)*100-100, 2)

mayoresVolumenes = data[(data['volume'] > (volHistMed*5))]

print(mayoresVolumenes)