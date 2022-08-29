import csv
data = csv.reader(open('estado_resultados.csv'),delimiter=';')
balances = []
comp = {}
count = 0

for fila in data:
	balances.append(fila)
	comp[fila[0]]=False

balances.pop(0)

for i in balances:
	if i[1] == "anual" and comp[i[0]]==False:
		try:
			RD = int(i[3]) > 1000000000
			count+=1
			comp[i[0]]=True
		except:
			continue	



print(count)	