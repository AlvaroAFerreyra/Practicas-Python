import csv
data = csv.reader(open('estado_resultados.csv'),delimiter=';')
balances = []
ebit = []


for fila in data:
	balances.append(fila)

for i in balances:
	if balances[fila][0]=="AAPL":
		AAPL.append(fila)
