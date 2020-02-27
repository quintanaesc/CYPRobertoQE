
########
archivo=open("numeros.txt","rt")
print(dir(archivo))

numeros1=archivo.read()
print(numeros1)
print(numeros1.split('\n'))
lista_num=[]
for line in numeros1.split('\n'):
    for numero in line.split(','):
        lista_num.append(int(numero))
print(lista_num)
lista_num.sort()
print(f"\n lista ortdenada: {lista_num} \n")

##################
print("******")


archivo=open("numeros.txt","rt")
numeros2=archivo.readlines()

print(numeros2)
archivo.close()

##########
print("-----")

archivo=open("numeros.txt","rt")
numeros3=archivo.readline()

print(numeros3)

archivo.close()

############
print("******")

archivo=open("numeros.txt","rt")
numeros4=archivo.readlines()
print(numeros4)
lista2=[]

for n in numeros4:
    for nums in n.split(","):
        lista2.append(int(nums))

print(lista2)
lista2.sort()
print(lista2)
archivo.close()
