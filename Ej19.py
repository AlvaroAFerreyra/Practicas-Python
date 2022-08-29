import csv
data = csv.reader(open('estado_resultados.csv'),delimiter=';')
balances = []
empresas = []
TF = {}

for fila in data:
	if fila[0] != "symbol":
		balances.append(fila)

for i in balances:
	TF[i[0]] = False

for empresa in balances:
	try:
		ratio = int(empresa[21])/int(empresa[19]) < 0.5
	except:
		ratio = False	
	try:
		rd = int(empresa[3]) > 5000000000 
	except:
		rd = False	
	if ratio and rd and empresa[1]=="anual" and TF[empresa[0]]==False:
		print(empresa[0])
		TF[empresa[0]] = True	

