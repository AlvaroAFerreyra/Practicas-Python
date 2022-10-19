import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

i=0
a=0

empresas = ['BBAR','BMA','CRESY','EDN','GGAL','PAM','TEO','TGS','YPF']

for empresa in empresas:
	empresas[i] = pd.read_excel(empresa+'.xlsx')
	i=i+1

for a in range(len(empresas)):
	empresas[a] = empresas[a][(empresas[a].timestamp > '2012-12-31') & (empresas[a].timestamp < '2014-1-1')]
	empresas[a]['varDiaria'] = empresas[0].adjusted_close.pct_change(-1)*100
	print(empresas[a])
	a=a+1