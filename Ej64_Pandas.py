import pandas as pd
import datetime as dt

data = pd.read_excel("AAPL.xlsx")

data.drop(["open",'close','volume','high','low'], axis=1, inplace=True)

data.set_index("timestamp", inplace=True)

data = data.sort_values("timestamp", ascending=True)

ruedas = int(input("Ingrese el número de ruedas: "))

desvios = int(input("Ingrese el número de desvios: "))

data["var"] = data.adjusted_close.pct_change()*100

data['desvio'] = data.adjusted_close.rolling(ruedas).std()

data['mediaMov'] = data.adjusted_close.rolling(ruedas).mean()

data["supBollinger"] = data.mediaMov + data.desvio*desvios

data["lowBollinger"] = data.mediaMov - data.desvio*desvios

newTable['fecha'] = data.timestamp

newTable['cierreAjustado'] = data.adjusted_close

newTable['supBollinger'] = data.supBollinger

newTable['lowBollinger'] = data.lowBollinger 

print(newTable.dropna())

