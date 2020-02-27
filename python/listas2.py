#areglos
#lectura
#escritura/asignacion
#actualizacion: insercion, eliminacion, modificacion
#ordenamiento
#busqueda

#escritura

frutas=["Zapote","Manzana","Pera","Aguacate","Durazno","Uva","Sandia"]

#lectura, el selector [indice]

print(frutas[2])
print("-----")
#for opcion 1
for indice in range(0,7,1):
    print(frutas[indice])
print("-----")
#for opcion 2: por interador for each
for fr in frutas:
    print(fr)
print("-----")


#asignacion
frutas[2]="Melon"
print(frutas)
print("-----")

#insercion al final

frutas.append("Naranja")
print(frutas)
##nota: escribir dir(list) para ver mas funciones para lista, con help(list.nombredelafuncion) obtenemos una descripcion de la funcion
frutas.insert(2,"limon")
print(frutas[2])
frutas.insert(0,"Mamey")
print(frutas)
#eliminacion con pop
print(frutas.pop())
print(frutas)
print(frutas.pop(1))
print(frutas)

#eliminar con remove
##insertamos otro limon a listas
frutas.append("limon")
frutas.append("limon")
print(frutas)
frutas.remove("limon")
print(frutas)

#ordenamiento
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)

#busqueda
print(f"el limon esta en la posicion {frutas.index('Uva')}")
print(f"el limon esta {frutas.count('limon')} veces en la lista")

#concatenar
print(frutas)
otras_frutas=["Rambutan","Mispero","Liche","Pitaya"]
print(otras_frutas)
frutas.extend(otras_frutas)
print(frutas)

#copia
##copia referencia de memoria(lo que hagas en una se hara en otra)
copia=frutas
copia.append("naranja")
print(frutas)
print(copia)
##copia informacion(si hay modificacion en la copia no se reflejara en informacion)
otra_copia=frutas.copy()
otra_copia.append("Fresa")
print(frutas)
print(otra_copia)
