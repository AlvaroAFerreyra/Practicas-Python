import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

data["var_porc_diaria"] = round((data.close-data.open)/data.open*100, 2)

data.to_excel("AAPL_ej.xlsx", sheet_name="Ej3", columns=["timestamp","var_porc_diaria"])