import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')
data["var_porc_diaria"] = (data.close-data.open)/data.open*100

data = data.drop(["volume","adjusted_close"], axis=1).head()
print(data)


