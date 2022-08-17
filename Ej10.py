import csv
data = csv.reader(open('SPY.csv'),delimiter=';')
cierresSPY = []
aperturasSPY = []
for fila in data:
	cierresSPY.append(fila[4])
	aperturasSPY.append(fila[1])

for i in range(1,6):
	gap = round(((float(aperturasSPY[i+1])/float(cierresSPY[i]))-1)*100,2) 	
	print(gap)


