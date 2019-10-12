CA=int(input("Ingrese la categoria del trabajador del 1 al 8: "))
SB=float(input("Ingrese el sueldo base del tabajador: $"))
HT=int(input("Ingrese las horas extras trabajadas redondeadas al entero menor inmediato: "))
if CA==1:
    PE=30
elif CA==2:
    PE=38
elif CA==3:
    PE=50
elif CA==4:
    PE=70
elif CA<=8:
    PE=0
    if HT>0:
        print("Su nivel de empleado es demasiado alto, ya para que hace horas extraa, no se las  van a pagar :´V")
else:
    PE=-1
    if HT>0:
        print("Usted ni trabaja en esta empreza y  aun asi hace horas extra :V?")
if PE>0:
    ST=SB+PE
else:
    ST=SB
print(f"Su sueldo total es de ${ST}")
print("fin del programa")
