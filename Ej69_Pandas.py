import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

listaVar = []

empresas = ['BBAR','BMA','CRESY','EDN','GGAL','PAM','TEO','TGS','YPF']

for empresa in empresas:
	tabla = pd.read_excel(empresa+'.xlsx')
	tabla = tabla.sort_values('timestamp', ascending=True)
	tabla['varDiaria'] = tabla.adjusted_close.pct_change()*100
	tabla.set_index('timestamp', inplace=True)
	listaVar.append(tabla['varDiaria'])

newDF = pd.concat(listaVar, axis=1)

newDF.columns = empresas

newDF = newDF.loc[(newDF.index >= '2013-01-01') & (newDF.index <= '2013-12-31')]

print(newDF)	

