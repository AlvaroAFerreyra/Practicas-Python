import csv
data = csv.reader(open('estado_resultados.csv'),delimiter=';')
AAPL_RD = []
listaSum = []

for fila in data:
	if fila[0]=="AAPL" and fila[1]=="trimestral":
		AAPL_RD.append(fila[3])

for i in range(10):
	listaSum.append(int(AAPL_RD[1]))	

print(sum(listaSum)/10/1000000000)		