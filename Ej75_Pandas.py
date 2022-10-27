import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_excel("ADRsHIST.xlsx")
data.set_index('timestamp', inplace=True)

pr = data.columns.std()-2.5

print(pr)