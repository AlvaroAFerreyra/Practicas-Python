activos1=["ALUA","BMA","BYMA","CEPU","COME","CRES","CVH","EDN","GGAL","MIRG"]
activos2=["PAM","SUPV","TECO2","TGNNO4","TGSU2","TRAN","TXAR","VALO","YPF"]
activos1.extend(activos2)
totalActivos=activos1

activoBuscado=input("Ingrese el activo buscado: ").upper()

if (activoBuscado in totalActivos):
    print(f"El activo {activoBuscado} se encuentra dentro de la variable")
else:
    print(f"El activo {activoBuscado} no se encuentra en la lista")   