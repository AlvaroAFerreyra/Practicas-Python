import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_excel("AAPL.xlsx")
data.sort_values("timestamp", ascending=True)
data.set_index('timestamp', inplace=True)

data['varstd'] = data.adjusted_close.pct_change().rolling(20).std()
data['varstd_c'] = data.adjusted_close.rolling(20).std()
data['volatilidad'] = data.varstd * 20 ** 0.5
data['sma20'] = data.adjusted_close.rolling(20).mean()
data['bollingerSup'] = data.sma20 + 2.5 * data.varstd_c
data['bollingerInf'] = data.sma20 - 2.5 * data.varstd_c

data = data.dropna()
data = data.loc[data.index >= '2019']

fig, ax0 = plt.subplots(figsize=(10,5))

plt.gca().set_yscale('log')
plt.plot(data.sma20)
plt.fill_between(data.index, data.bollingerInf, data.bollingerSup, alpha=0.2)

ax1= plt.gca().twinx()
ax1.set_ylabel('volatilidad')
ax1.plot(data.volatilidad, ls='--')

plt.show() 

