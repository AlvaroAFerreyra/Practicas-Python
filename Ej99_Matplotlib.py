import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import mplfinance as mpf

adr = input("Inserte el ADR buscado: ").upper()
año = int(input("Inserte el año buscado: "))
trimestre = int(input("Inserte el trimestre buscado: "))

if trimestre == 1:
	principio = dt.datetime(año,1,1)
	fin = dt.datetime(año,4,1)
elif trimestre == 2:
	principio = dt.datetime(año,4,1)
	fin = dt.datetime(año,7,1)
elif trimestre == 3:
	principio = dt.datetime(año,7,1)
	fin = dt.datetime(año,10,1)
elif trimestre == 4:
	principio = dt.datetime(año,10,1)
	fin = dt.datetime(año+1,1,1)	
else: print("Q fuera de rango")	