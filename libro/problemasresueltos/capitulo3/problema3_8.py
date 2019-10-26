NUM=int(input("Ingrese un numero entero positivo: "))
if NUM>0:
    while NUM<1 or NUM>1:
        print(NUM)
        if ((-1)**NUM)>0:
            NUM=NUM/2
        else:
            NUM=NUM*3+1
    print(NUM)
else:
    print("El numero tiene que ser un entero positivo")
print("fin del programa")
