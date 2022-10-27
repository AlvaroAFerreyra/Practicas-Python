import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

empresas = ['BBAR','BMA','CRESY','EDN','GGAL','PAM','TEO','TGS','YPF']

listavn = []

data = pd.read_excel("ADRsHIST.xlsx")
data.set_index('timestamp', inplace=True)

for empresa in empresas:

	vn = data[empresa].quantile(0.01)
	listavn.append(vn)

grafico = pd.DataFrame(index=data.columns)

grafico['varNeg'] = listavn 

fig, ax=plt.subplots()
ax.bar(grafico.index, grafico.varNeg)
plt.show()