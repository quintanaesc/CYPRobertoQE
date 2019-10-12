TF=int(input("Ingrese el tipo de enfermedad del paciente (del 1 al 4): "))
ED=int(input("ingrese la edad del paciente: "))
DI=int(input("Ingrese el numero de dias que permanecio el paciente en el hospital: "))
if TF==1:
    CT=DI*25
elif TF==2:
    CT=DI*16
elif TF==3:
    CT=DI*20
elif TF==4:
    CT=DI*32
else:
    print("Enfermedad no registrada, mejor empiece a rezar")
if TF>=1 and TF<=4:
    if ED>=14 and ED<=22:
        CT=CT*1.10
    print(f"Su costo total es de ${CT}")
print("fin del programa")
