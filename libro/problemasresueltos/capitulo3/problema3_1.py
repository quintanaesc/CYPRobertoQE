SI=0
SP=0
CP=0
CI=0
print("Ingrese 270 numeros: ")
for I in range (1,271,1):
    N=int(input(""))
    if N<0 or N>0:
        if ((-1)**N)>0:
            SP+=N
            CP=CP+1
        else:
            SI+=N
            CI+=1
if CP<0 or CP>0:
    PP=SP/CP
else:
    PP=0
print(f"La cantidad de numeros impares ingresados es de {CI} y la suma d ellos es de {SI}")
print(f"La cantidad de numeros pares ingresados es de {CP} y su promedio es de{PP}")
