import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

bollinger = pd.read_excel("tablaBollinger.xlsx")

tablaFiltrada = bollinger[(bollinger.cierreAjustado > bollinger.supBollinger) | (bollinger.cierreAjustado < bollinger.lowBollinger)]

tablaFiltrada.set_index('timestamp', inplace=True)

conteo = tablaFiltrada.cierreAjustado.groupby(tablaFiltrada.index.year)

conteo = conteo.count().to_frame()

print(conteo.plot.bar())