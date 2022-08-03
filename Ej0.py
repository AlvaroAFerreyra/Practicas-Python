smaFast=100
smaSlow=98
buyPrice=106
price=128

tendencia=smaFast>smaSlow*1.02
stopLoss=price<buyPrice*0.95
stopWin=price>buyPrice*1.2

if (tendencia and not stopLoss and not stopWin):
	hold=True
else: hold=False

print (hold)	