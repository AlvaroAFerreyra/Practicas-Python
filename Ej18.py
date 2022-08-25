import csv
data = csv.reader(open('estado_resultados.csv'),delimiter=';')
balances = []
empresas = ["FB","AMZN","AAPL","NFLX","GOOGL"]
search = {}

for fila in data:
	if fila[0] in empresas:
		search[fila[0]] = False

for busqueda in data:
	if busqueda[0] in empresas and busqueda[1]=="anual" and search[busqueda[0]]==False:
		try:
			print(f"El ratio de {busqueda[0]} es {int(busqueda[20])/int(busqueda[7])}")
			search[busqueda[0]]==True
		except:
			print("No se pudo calcular")	

