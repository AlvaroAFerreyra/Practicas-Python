import csv
data = csv.reader(open('SPY.csv'),delimiter=';')
cierresAjustadosSPY = []
varPos = []
varNeg = []
varNeu = []
countPos = 0
countNeg = 0
countNeu = 0
countTot = 0
dic = {}
variacion = []


for fila in data:
	cierresAjustadosSPY.append(fila[5])
cierresAjustadosSPY.pop(0)	

for i in range(len(cierresAjustadosSPY)):
	try:
		variacion.append(float(cierresAjustadosSPY[i+1])-float(cierresAjustadosSPY[i]))
	except:
		pass	

for j in variacion:
	if j>0:
		varPos.append(j)
		countPos+=1
	elif j<0:
		varNeg.append(j)
		countNeg+=1
	else:
		varNeu.append(j)
		countNeu+=1	
	countTot+=1		

dic["promedioPositivos"] = round((sum(varPos)/countPos), 2)
dic["promedioNegativos"] = round((sum(varNeg)/countNeg), 2)
dic["porcentajePositivos"] = (round(len(varPos)/countTot, 2))*100
dic["porcentajeNegativos"] = (round(len(varNeg)/countTot, 2))*100
dic["porcentajeNeutros"] = (round(len(varNeu)/countTot, 2))*100 

print(dic)


