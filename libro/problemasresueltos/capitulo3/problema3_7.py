MED=0
CHI=0
GRA=0
N=int(input("Ingrese la cantidad de valores con los que vamos a trabajar: "))
for I in range (1,N+1,1):
    V=float(input("Ingrese el valor de la venta realizada: $"))
    if V<=200:
        CHI+=1
    elif V<400:
        MED+=1
    else:
        GRA+=1
print("Las ventas menores o iguales a $200 fueron: ",CHI)
print("Las ventas menores a $400 pero mayores a $200 fueron: ",MED)
print("Las ventas mayores a $400 fueron: ",GRA)
print("fin del programa")
