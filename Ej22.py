import csv
data = csv.reader(open('estado_resultados.csv'),delimiter=';')
balances = []

for fila in data:
	print(fila[0])