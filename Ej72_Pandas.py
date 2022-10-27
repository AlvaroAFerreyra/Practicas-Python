import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_excel("ADRs2013.xlsx")

data.set_index('timestamp', inplace=True)

rendimiento = data.mean()
desvio = data.std()
TLR = 0.03 / 360

newTable = pd.DataFrame(index = data.columns)

newTable['sharpeDiario'] = (rendimiento - TLR) / desvio

newTable['sharpeAnual'] =  newTable.sharpeDiario * 250**0.5

fig, ax=plt.subplots()
ax.bar(newTable.index, newTable.sharpeAnual)
plt.show()