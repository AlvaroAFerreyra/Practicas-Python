import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('SPY.xlsx')
data.set_index('timestamp', inplace=True)


graf2014 = data.loc[(data.index >= "2014-01-01") & (data.index <= "2014-12-31")]
graf2015 = data.loc[(data.index >= "2015-01-01") & (data.index <= "2015-12-31")]


fig, gf1=plt.subplots(figsize=(10,4))
gf1.plot(graf2014.index, graf2014.adjusted_close, color='g')
gf2 = gf1.twiny()
gf2.plot(graf2015.adjusted_close, color='r')
plt.legend(['2014','2015'], loc='lower right')
plt.show()

