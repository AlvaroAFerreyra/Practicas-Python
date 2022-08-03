smaFast=100
smaSlow=98
buyPrice=106

tendencia=smaSlow*1.02
tendenciaBull=smaFast>tendencia
stopLoss=buyPrice*0.95
stopWin=buyPrice*1.2

if (tendenciaBull==True and buyPrice>stopLoss and buyPrice<=stopWin):
	hold=True
else: hold=False

print (hold)	