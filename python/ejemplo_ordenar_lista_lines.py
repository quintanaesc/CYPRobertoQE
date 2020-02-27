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
