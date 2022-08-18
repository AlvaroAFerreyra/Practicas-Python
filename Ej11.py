import csv
data = csv.reader(open('SPY.csv'),delimiter=';')
cierresSPY = []
aperturasSPY = []
gaps= []
positivos=0
negativos=0
neutros=0

for fila in data:
	cierresSPY.append(fila[4])
	aperturasSPY.append(fila[1])

for i in range(1,len(aperturasSPY)):
	try:
		gap = round(((float(aperturasSPY[i+1])/float(cierresSPY[i]))-1)*100,2) 	
	except:
		gap = 0	
	gaps.append(gap)

for g in gaps:
	if g>0:
		positivos+=1
	elif g<0:
		negativos+=1
	else:
		neutros+=1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Neutros: {neutros}")
