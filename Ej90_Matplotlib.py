import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_excel('AAPL.xlsx')
data = data.sort_values('timestamp', ascending=True)
data['gap'] = (data.open / data.adjusted_close.shift(1)-1)*100
data['intra'] = (data.adjusted_close / data.open-1)*100
cleanTable = data.drop(['high','low','volume','close','open','adjusted_close'], axis=1)
cleanTable = cleanTable.dropna().set_index('timestamp')

años = ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
gapsAnualizados = cleanTable['gap'].groupby(cleanTable.index.year).mean()
intraAnualizado = cleanTable['intra'].groupby(cleanTable.index.year).mean()

print(gapsAnualizados)

fig, ax = plt.subplots(figsize = (10,5))
ax.plot(gapsAnualizados)
ax.plot(intraAnualizado)
ax.legend(['Gaps','Intradiarios'], loc="lower right")



plt.show()