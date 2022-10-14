import pandas as pd
import datetime as dt

bollinger = pd.read_excel("tablaBollinger.xlsx")

bollinger.set_index("timestamp", inplace=True)

bollinger['superior'] = bollinger.cierreAjustado > bollinger.supBollinger

bollinger['inferior'] = bollinger.cierreAjustado < bollinger.lowBollinger

print(bollinger.superior.resample("Y").sum().to_frame())

print(bollinger.inferior.resample("Y").sum().to_frame())

print(bollinger.dropna())