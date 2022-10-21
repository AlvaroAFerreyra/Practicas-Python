import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_excel("ADRs2013.xlsx")

data.set_index('timestamp', inplace=True)

newTable = pd.DataFrame(index = data.columns)

newTable['rendAcum'] = (((data/100+1).prod()-1)*100)

newTable['volatilidadAnual'] = data.std() * (len(data)**0.5)

print(newTable)

