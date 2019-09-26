SUE=float(input("Ingrese su sueldo base: $"))
if SUE<1000:
	NSUE=SUE*1.15
else:
	NSUE=SUE*1.12
print(f"Su sueldo total es de ${NSUE}")

