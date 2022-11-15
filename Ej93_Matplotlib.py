import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_excel("AAPL.xlsx")
data.sort_values("timestamp", ascending=True)
data.set_index('timestamp', inplace=True)

print(data)