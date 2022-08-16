import csv
data = csv.reader(open('SPY.csv'),delimiter=';')
cierresSPY = []
for fila in data:
	cierresSPY.append(fila[4])

print(cierresSPY[0:10])	