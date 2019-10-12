MAT=int(input("Ingrese la matricula del alumno: "))
CAR=str(input("Ingrese la carrera inscrita por el alumno (unicamente mayusculas): "))
SEM=int(input("Ingrese el ultimo semestre aprobado: "))
PRO=float(input("Ingrese su promedio: "))
if CAR=="ECONOMIA":
    if SEM>=6 and PRO>=8.8:
        print(f"El alumno con matricula {MAT} inscrito en la carrera de {CAR} fue ´ACEPTADO´ ")
    else:
         print(f"El alumno con matricula {MAT} inscrito en la carrera de {CAR} fue ´RECHAZADO´ ")
elif CAR=="COMPUTACION":
    if SEM>6 and PRO>8.5:
        print(f"El alumno con matricula {MAT} inscrito en la carrera de {CAR} fue ´ACEPTADO´ ")
    else:
         print(f"El alumno con matricula {MAT} inscrito en la carrera de {CAR} fue ´RECHAZADO´ ")
elif CAR=="CONTABILIDAD"  or CAR=="ADMINISTRACION":
    if SEM>5 and PRO>8.5:
         print(f"El alumno con matricula {MAT} inscrito en la carrera de {CAR} fue ´ACEPTADO´ ")
    else:
         print(f"El alumno con matricula {MAT} inscrito en la carrera de {CAR} fue ´RECHAZADO´ ")
else:
    print("Usted ingreso una carrera no registrada intentelo más tarde")
print("fin del programa")
