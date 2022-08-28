import csv
data = csv.reader(open('estado_resultados.csv'),delimiter=';')
balances = []
empresas = ["FB","AMZN","AAPL","NFLX","GOOGL"]
search = {}

for fila in data:
	balances.append(fila)
	if fila[0] in empresas:
		search[fila[0]] = False

for busqueda in balances:
	if busqueda[0] in empresas and busqueda[1]=="anual" and search[busqueda[0]]==False:
		try:
			search[busqueda[0]] = round(int(busqueda[21])/int(busqueda[19]), 2)
		except:
			print("No se pudo calcular")	
	else:
		continue

print(search)