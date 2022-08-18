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
posCount = 0
negCount = 0
neuCount = 0
iPosCount = 0
iNegCount = 0

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
		gPositivos=gPositivos+g
		posCount+=1
	elif g<0:
		gNegativos=gNegativos+g
		negCount+=1
	else:
		neuCount+=1

for j in intraDays:
	if j>0:
		iPositivos=iPositivos+j
		iPosCount+=1
	elif j<0:
		iNegativos=iNegativos+j
		iNegCount+=1
	else:
		iNeutros+=1

promGapsPos = round(gPositivos/posCount, 2)
promGapsNeg = round(gNegativos/negCount, 2)

print(f"El promedio de los gaps positivos es: {promGapsPos}")
print(f"El promedio de los gaps negativos es: {promGapsNeg}")


porcGapsPos = round(posCount/len(gaps)*100, 2)
porcGapsNeg = round(negCount/len(gaps)*100, 2)

print(f"El porcentaje de gaps positivos sobre el total es: {porcGapsPos}%")
print(f"El porcentaje de gaps negativos sobre el total es: {porcGapsNeg}%")


promIntraPos = round(iPositivos/iPosCount, 2)
promIntraNeg = round(iNegativos/iNegCount, 2)

print(f"El promedio de los intradiarios positivos es: {promIntraPos}")
print(f"El promedio de los intradiarios negativos es: {promIntraNeg}")

porcIntraPos = round(iPosCount/len(intraDays)*100, 2)
porcIntraNeg = round(iNegCount/len(intraDays)*100, 2)

print(f"El porcentaje de intradays positivos sobre el total es: {porcIntraPos}%")
print(f"El porcentaje de intradays negativos sobre el total es: {porcIntraNeg}%")
