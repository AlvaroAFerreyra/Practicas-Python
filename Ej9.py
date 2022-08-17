import csv
data = csv.reader(open('SPY.csv'),delimiter=';')
cierresSPY = []
for fila in data:
	cierresSPY.append(fila[4])

count = 0
for i in range(len(cierresSPY)):
	try:
		gap = float(cierresSPY[i])/float(cierresSPY[i+1])>1.05
		if gap:
			count+=1	
	except:
		continue	

print(count)
print(len(cierresSPY))