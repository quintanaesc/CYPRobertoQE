MAY=-100000
MEN=100000
N=int(input("Ingrese la cantidad de valores con los que vamos a trabajar: "))
for I in range (1,N+1,1):
    NUM=int(input("Ingrese un numero entero entre el -100000 y el 100000: "))
    if NUM>MAY:
        MAY=NUM
    if NUM<MEN:
        MEN=NUM
print(f"El numero mayor es {MAY} mientras que el menor es {MEN}")
print("fin del programa")
