import csv
data = csv.reader(open('estado_resultados.csv'),delimiter=';')
balances = []
empresas = ["FB","AMZN","AAPL","NFLX","GOOGL"]
search = {}

for fila in data:
	if fila[0] in empresas:
		search[fila[0]] = False

print(search)		