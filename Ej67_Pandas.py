import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

newTable = pd.DataFrame()

bollinger = pd.read_excel("tablaBollinger.xlsx")

bollinger['precioForward'] = bollinger.cierreAjustado.shift(-5)

bollinger['varForward'] = (bollinger.precioForward / bollinger.cierreAjustado -1)*100

newTable = bollinger.loc[bollinger.cierreAjustado > bollinger.supBollinger]

print(newTable.varForward.mean())
