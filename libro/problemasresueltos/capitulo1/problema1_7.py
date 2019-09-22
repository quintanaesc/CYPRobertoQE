print("Mi funcion es calcular el area de un triangulo")
L1=float(input("Proporcione el primer lado en cm "))
L2=float(input("Proporcione el segundo lado en cm "))
L3=float(input("Proporcione el ultimo lado en cm ")) 
S=(L1+L2+L3)/2
AREA=(S*(S-L1)*(S-L2)*(S-L3))**(1/2)
print(f"El area del triangulo es {AREA} cm^2")
