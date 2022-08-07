cartera={"AAPL":30,"AMZN":25,"NFLX":20,"FB":10,"KO":5,"USD":10}

ticker=input("Ingrese el activo buscado: ").upper()

if (ticker in cartera):
	print(f"Usted posee un {cartera[ticker]}% de {ticker} en su cartera")
else:
	print("No posee ese activo en cartera")	