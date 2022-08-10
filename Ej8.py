activos1=["ALUA","BMA","BYMA","CEPU","COME","CRES","CVH","EDN","GGAL","MIRG"]
activos2=["PAM","SUPV","TECO2","TGNNO4","TGSU2","TRAN","TXAR","VALO","YPF"]
activos1.extend(activos2)
totalActivos=activos1
precios={"GGAL":80,"YPF":500}

maxPerdida=0

stopLargo=8<maxPerdida<=15
stopSemiLargo=6<maxPerdida<=8
stopStandar=3<maxPerdida<=6
stopCorto=1<maxPerdida<=3

if(stopLargo):
	tipo="stopLargo"
	print(tipo)
elif(stopSemiLargo):
	tipo="stopSemiLargo"
	print(tipo)
elif(stopStandar):	
	tipo="stopStandar"
	print(tipo)
elif(stopCorto):
	tipo="stopCorto"
	print(tipo)
else: 
	tipo="Fuera de rango"
	print(tipo)			


