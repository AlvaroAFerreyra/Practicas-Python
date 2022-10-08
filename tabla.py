import pandas as pd
import datetime as dt

activos = ["AAPL","SPY","QQQ"]

listaVariaciones = []

for activo in activos:
	tabla = pd.read_excel(str(activo)+'.xlsx')
	tabla = sort_values('timestamp', ascending=True)
	tabla['change_pct'] = tabla['adjusted_close'].pct_change()*100
	tabla.set_index('timestamp', inplace=True)
	listaVariaciones.append(tabla['change_pct'])

tablaFinal = pd.concat(listaVariaciones, axis=1).dropna()
tablaFinal.columns = activos
tablaFinal.to_excel("AAPL_SPY_QQQ.xlsx")	