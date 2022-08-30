import csv
data = csv.reader(open('estado_resultados.csv'),delimiter=';')
balances = []
limit = {}
lista_id = []

for empresa in data:
	limit[empresa[0]] = False
	balances.append(empresa)

balances.pop(0)

for search in balances:
	if limit[search[0]]==False and search[1]=="anual":
		try:
			lista_id.append(int(search[3]))	
			limit[search[0]]=True		
		except:
			continue

print(sum(lista_id)/len(lista_id)/1000000)		