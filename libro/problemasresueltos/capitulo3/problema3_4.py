NOM=0
SUE=float(input("Ingrese el sueldo del empleado (ingrese -1 para detener el programa): "))

while SUE<-1 or SUE>-1:
    if SUE<1000:
        NSUE=SUE*1.15
    else:
        NSUE=SUE*1.15
    NOM+=NSUE
    print(f"El nuevo sueldo es de: {NSUE}")
    SUE=float(input("Ingrese el sueldo del empleado (ingrese -1 para detener el programa): "))
print(f"La nueva nomina total es de: {NOM}")
print(f"fin del programa")
