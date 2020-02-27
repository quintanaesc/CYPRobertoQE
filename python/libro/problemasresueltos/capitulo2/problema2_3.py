print("Dada la ecuacion (Ax^2)+Bx+C")
A=float(input("Ingrese el coeficiente A "))
B=float(input("Ingrese el coeficiente B "))
C=float(input("Ingrese el coeficiente C "))
DIS=(B**2)-4*A*C
if DIS>=0:
	x1=(-B+DIS**0.5)/(2*A)
	x2=(-B-DIS**0.5)/(2*A)
	print(f"Las soluciones reales de la ecuacion son {x1} & {x2}")
print("fin del programa")
