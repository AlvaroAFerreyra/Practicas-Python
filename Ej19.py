import csv
data = csv.reader(open('estado_resultados.csv'),delimiter=';')
balances = []
empresas = []

for fila in data:
	if fila[0] != "symbol":
		balances.append(fila)

for empresa in balances:
	try:
		ratio = int(empresa[21])/int(empresa[19]) < 0.5
	except:
		ratio = False	
	try:
		rd = int(empresa[3]) > 5000000000000 
	except:
		rd = False	
	if ratio and rd and empresa[1]=="anual":
		print(f"{empresa[0]} ratio:{ratio} R+D:{rd}")

