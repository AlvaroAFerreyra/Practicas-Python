import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

i=0
o=0

empresas = ['BBAR','BMA','CRESY','EDN','GGAL','PAM','TEO','TGS','YPF']

for empresa in empresas:
	empresas[i] = pd.read_excel(empresa+'.xlsx')
	"""empresas[i].set_index('timestamp', inplace=True)"""
	i=i+1

for o in range(len(empresas)):
	empresas[o] = empresas[o][(empresas[o].timestamp > '2012-12-31') & (empresas[o].timestamp < '2014-1-1')]
	print(empresas[o])
	o=o+1