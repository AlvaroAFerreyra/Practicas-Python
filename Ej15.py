import csv
data = csv.reader(open('estado_resultados.csv'),delimiter=';')
encabezadosColumnas = []


for fila in data:
	encabezadosColumnas.append(fila)

print(encabezadosColumnas[0])
