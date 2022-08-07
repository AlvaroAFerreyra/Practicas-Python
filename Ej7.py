activos1=["ALUA","BMA","BYMA","CEPU","COME","CRES","CVH","EDN","GGAL","MIRG"]
activos2=["PAM","SUPV","TECO2","TGNNO4","TGSU2","TRAN","TXAR","VALO","YPF"]
activos1.extend(activos2)
totalActivos=activos1
precios={"GGAL":80,"YPF":500}

ticker=input("Ingrese el activo buscado: ").upper()

if (ticker in precios):
	print(f"El precio de {ticker} es {precios[ticker]}")
elif (ticker in totalActivos):
	print(f"El activo {ticker} no tiene precios asignado")
else: 
	print(f"El activo {ticker} no se encuentra en el listado")


