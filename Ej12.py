import csv
data = csv.reader(open('SPY.csv'),delimiter=';')
cierresSPY = []
aperturasSPY = []
gaps= []
gPositivos = 0
gNegativos = 0
gNeutros = 0
intraDays = []
iPositivos = 0
iNegativos = 0
iNeutros = 0

for fila in data:
	cierresSPY.append(fila[4])
	aperturasSPY.append(fila[1])

for i in range(1,len(aperturasSPY)):
	try:
		gap = round(((float(aperturasSPY[i+1])/float(cierresSPY[i]))-1)*100,2) 	
	except:
		gap = 0	
	gaps.append(gap)

for h in range(1,len(aperturasSPY)):
	try:
		intraDay = round(((float(cierresSPY[h])/float(aperturasSPY[h]))-1)*100,2)
	except:
		intraDay = 0
	intraDays.append(intraDay)		


for g in gaps:
	if g>0:
		gPositivos+=1
	elif g<0:
		gNegativos+=1
	else:
		gNeutros+=1

for j in intraDays:
	if j>0:
		iPositivos+=1
	elif j<0:
		iNegativos+=1
	else:
		iNeutros+=1

print("GAPS")
print(f"Positivos: {gPositivos}")
print(f"Negativos: {gNegativos}")
print(f"Neutros: {gNeutros}")
print("INTRADIARIOS")
print(f"Positivos: {iPositivos}")
print(f"Negativos: {iNegativos}")
print(f"Neutros: {iNeutros}")