print("Incerte las cordenadas del un punto en el plano") 
X1=float(input(" Cordenada X:")) 
Y1=float(input(" Cordenada Y:"))
print("Incerte las cordenadas de un segundo punto") 
X2=float(input(" Cordenada en X:")) 
Y2=float(input(" Cordenada en Y:"))
DIS=(((X1-X2)**2)+((Y1-Y2)**2))**(1/2)
print(f"La distancia entre el punto ({X1},{Y1}) y ({X2},{Y2}) es {DIS}")