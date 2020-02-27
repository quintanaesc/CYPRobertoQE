N=int(input("Ingrese un numero entero: "))
SERIE=0
I=1
BAND="T"
for I in range (1,N+1,1):
    if BAND=="T":
        SERIE+=1/I
        BAND="F"
    else:
        SERIE+=-1/I
        BAND="T"
print(f"LA suma de la serie es de: {SERIE}")
print("fin del programa")
