MAT=int(input("Ingrese la matricula del alumno "))
CAL1=float(input("Ingrese su primera calificacion "))
CAL2=float(input("Ingrese su segunda calificacion "))
CAL3=float(input("Ingrese su tercera calificacion "))
CAL4=float(input("Ingrese su cuarta calificacion "))
CAL5=float(input("Ingrese su quinta calificacion "))
PRO=(CAL1+CAL2+CAL3+CAL4+CAL5)/5
if PRO>=6:
	print(f"El alumno con matricula {MAT} obtuvo un promedio de {PRO} por lo que APROBO")
else:
	print(f"El alumno con matricula {MAT} obtuvo un promedio de {PRO} por lo que REPROBO")
