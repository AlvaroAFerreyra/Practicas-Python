import pandas as pd
data = pd.read_excel('AAPL.xlsx',sheet_name='Hoja1')

dataDateIndex = data.set_index("timestamp")

print(dataDateIndex.loc["2008-05-15"])