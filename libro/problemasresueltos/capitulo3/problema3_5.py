SUMOTR=0
SUMPOS=0
CUEPOS=0
N=int(input("Ingrese la cantidad de valores con los que vamos a trabajar: "))
for I in range (1,N+1,1):
    NUM=int(input("Ingrese un numero entero: "))
    if NUM>0:
        SUMPOS+=NUM
        CUEPOS+=1
    else:
        SUMOTR+=NUM
PROGEN=(SUMPOS+SUMOTR)/N
PROPOS=SUMPOS/CUEPOS
print(f"LA cantidad de numeros positivos fue de: {CUEPOS}")
print(f"El Promedio de numeros total fue de: {PROPOS}")
print("El promedio de todos los numeros ingresados es de: ",PROGEN)
print("fin del programa")
