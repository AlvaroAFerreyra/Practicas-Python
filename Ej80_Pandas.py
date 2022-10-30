import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

empresas = ['BBAR','BMA','CRESY','EDN','GGAL','PAM','TEO','TGS','YPF']

data = pd.read_excel("ADRsHIST.xlsx")
data.set_index('timestamp', inplace=True)

data = data.corr(method="pearson").round(2)

data.replace(1, 0, inplace=True)

print(data.idxmax())