import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_excel("ADRs2013.xlsx")

newTable = pd.DataFrame()

rendAcum = []
volatAnual = []

empresas = ['BBAR','BMA','CRESY','EDN','GGAL','PAM','TEO','TGS','YPF']


data.set_index('timestamp', inplace=True)

for empresa in empresas:
	rendAcum.append(data[empresa].sum())
	volatAnual.append(data[empresa].std())

newTable['fecha'] = data.index

newTable['rendAcum'] = rendAcum

newTable['volatAnual'] = volatAnual

newTable.set_index('fecha', inplace=True)

newTable.columns = empresas

print(newTable)