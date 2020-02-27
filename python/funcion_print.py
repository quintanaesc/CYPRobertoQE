# print tiene 4 formas de uso
"""
1.- con comas
2.- con signo "+"
3.- con la funcion format()
4.- con una variante de format
"""
# con comas, concatenar agregando
# un espacio y haciendo casting de tipo

edad=10
nombre= "juan"
estatura=1.67
print(edad, estatura, nombre)

# con `+`hace lo mismo pero no
# realiza el casting automatico
# no agrega espacio
print( str(edad) + str(estatura) + nombre)

# funcion format()
print("nombre: {1} edad: {0}".format(nombre, edad))

# 4.-  con una variante de format() sinplificada
print(f"nombre:{nombre} \n edad: \t {edad}")

#print y el argumento end
print("solo hay 10 tipos de personas las que saben binario y las que no", end=" \`` ")
print("otra linea")
