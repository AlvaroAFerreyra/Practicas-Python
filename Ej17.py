import csv
data = csv.reader(open('estado_resultados.csv'),delimiter=';')
balances = []
costos = []
ingresos = []


for fila in data:
	if fila[0]=="AMZN" and fila[1]=="anual":
		costos.append(fila[21])
		ingresos.append(fila[19])

print(int(costos[1])/int(ingresos[1]))