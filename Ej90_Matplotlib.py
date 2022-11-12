import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_excel('AAPL.xlsx')
data = data.sort_values('timestamp', ascending=True)
data['gap'] = (data.open / data.close.shift(1)-1)*100
data['intra'] = (data.close / data.open-1)*100
cleanTable = data.drop(['high','low','volume','close','open','adjusted_close'], axis=1)
cleanTable = cleanTable.dropna().set_index('timestamp')

gapsAnualizados = cleanTable.gap.groupby(cleanTable.index.year).mean()
intraAnualizado = cleanTable.intra.groupby(cleanTable.index.year).mean()

print(gapsAnualizados)
print(intraAnualizado)

fig, ax = plt.subplots(figsize = (10,5))
ax.plot(gapsAnualizados)
ax.plot(intraAnualizado)
ax.legend(['Gaps','Intradiarios'], loc="lower right")

plt.show()