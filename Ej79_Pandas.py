import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

empresas = ['BBAR','BMA','CRESY','EDN','GGAL','PAM','TEO','TGS','YPF']

listavn = []

data = pd.read_excel("ADRsHIST.xlsx")
data.set_index('timestamp', inplace=True)

print(data.corr(method="pearson").round(2))