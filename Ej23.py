import pandas as pd
data = pd.read_csv('AAPL.csv',sep=",",index_col="timestamp")
print(data)


