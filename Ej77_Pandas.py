import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_excel("ADRsHIST.xlsx")
data.set_index('timestamp', inplace=True)

tabla = data.rank(pct=True, ascending=False).tail()*100

print(tabla.round(2))



