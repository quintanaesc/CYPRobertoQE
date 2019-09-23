print("Calculare el promedio de un alumno si me das sus 5 calificaciones")
MAT=int(input("Primero que nada ingresa tu matricula "))
CAL1=float(input("Dame su primera calificacion "))
CAL2=float(input("Dame la segunda calificacion "))
CAL3=float(input("Dame la tercera calificacion "))
CAL4=float(input("Dame la cuarta calificacion "))
CAL5=float(input("Dame la ultima calificacion "))
PRO=(CAL1+CAL2+CAL3+CAL4+CAL5)/5
print(f"El promedio del alumno con la matricula {MAT} es de {PRO}")
