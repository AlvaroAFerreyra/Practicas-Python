import pandas as pd
import datetime as dt
import matplotlib.pyplot as plot


bollinger = pd.read_excel("tablaBollinger.xlsx")

bollinger.set_index("timestamp", inplace=True)

bollinger['superior'] = bollinger.cierreAjustado > bollinger.supBollinger

bollinger['inferior'] = bollinger.cierreAjustado < bollinger.lowBollinger

newTable = pd.DataFrame(index = bollinger.index)

newTable['superior'] = bollinger.superior.resample("Y").sum().to_frame()

newTable['inferior'] = bollinger.inferior.resample("Y").sum().to_frame()

print(newTable.superior.dropna().plot(kind='bar'))

print(newTable.dropna())