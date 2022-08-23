import csv
data = csv.reader(open('estado_resultados.csv'),delimiter=';')
ebit = []


for fila in data:
	if fila[0]=="AAPL" and fila[1]=="trimestral":
		ebit.append(fila[10])

for i in range(4):
	print(int(ebit[i])/1000000)


