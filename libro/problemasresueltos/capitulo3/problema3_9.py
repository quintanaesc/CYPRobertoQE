SERIE=0
N=int(input("Ingrese un numero entero: "))
for I in range(1,N+1,1):
    SERIE=SERIE+I**I
print("El valor de la serie es: ",SERIE)
print("fin del programa")
