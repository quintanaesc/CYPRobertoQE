NU=int(input("Ingrese la cantidad de minutos que diro la llamada redondeada al entero siguiente: "))
CL=int(input("Ingrese la clave de su zona: "))
if CL==12:
    PR=2
    ZO="America del norte"
elif CL==15:
    PR=2.2
    ZO="America central"
elif CL==18:
    PR=4.5
    ZO="America del sur"
elif CL==19:
    PR=5.5
    ZO="Europa"
elif CL==23:
    PR=6
    ZO="Asia"
elif CL==25:
    PR=6
    ZO="Africa"
elif CL==29:
    PR=5
    ZO="Oceania"
else:
    PR=0
PT=PR*NU
if PT>0:
    print(f"Su total a pagar por la llamada de duracion de {NU} minutos es de ${PT}, con un costo por minuto de ${PR} al realizar la llamada en {ZO}")
else:
    print("LLamada demasiado corta o bien ingeso una Zona no valida")
print("fin del programa")
