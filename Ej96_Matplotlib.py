import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import mplfinance as mpf

adr = str(input("Inserte el ADR buscado: ")).upper()
año = str(input("Inserte el año buscado: "))

data = pd.read_excel(adr+".xlsx")
data.sort_values('timestamp', ascending=True)
data.set_index('timestamp', inplace=True)
data = data.loc[(data.index >= año) & (data.index < str(int(año)+1))]

print(data)