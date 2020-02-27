#listas
lluvias_norte=[80,60,120,100,70,150,100,47,95,70,100,130]
for indice in range(0,12,1):
    print(f"mes {indice+1} en region norte= {lluvias_norte[indice]}")
print(lluvias_norte[4])
#slaicing
print(lluvias_norte[:5:])
SUELDOS=[]
SUMA=0
for INDICE in range(7):
    SUELDOS.append(int(input("Sueldos")))
print(SUELDOS)
for INDICE in range(7):
    SUMA+=SUELDOS[INDICE]
PRO=SUMA/7
cont=0
print(f"El promedio de sueldos es {PRO}")
for INDICE in range(7):
    if SUELDOS[INDICE]>PRO:
        cont+=1
        print(f"Arriba: {SUELDOS[INDICE]}")
