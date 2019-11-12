archivo=open("numeros.txt","rt")
print(dir(archivo))

numeros1=archivo.read()
numeros1.replace("\n","")
print(numeros1)
print(numeros1.split('\n'))
lista_numeros=[]
for line in numeros.split('\n'):
    for numero in linea.split(','):
        list_num.append(int(numero))
print(lista_num)
list_num.sort()
print(f"\n lista ortdenada: {list_num} \n")
print("-----")

archivo.close()
archivo=open("numeros.txt","rt")
numeros2=archivo.readlines()

print(numeros2)
print("-----")
numeros3=archivo.readline()

print(numeros3)


