import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

data["var_porc_diaria"] = round((data.close-data.open)/data.open*100, 2)

pd.options.display.max_rows = 4

print(data)