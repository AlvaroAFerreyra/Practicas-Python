import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

listaFiltrada = pd.DataFrame() 

data = pd.read_excel("tablaBollinger.xlsx")

data['precioForward'] = data.adjusted_close.shift(-5)

data['varForward'] = (data.precioForward / data.adjusted_close -1)*100



print(data)