edad= int(input("Dame tu edad:"))
INE=bool(int(input("Tienes INE(0 no/ 1 si)?:")))
if edad>=18 and INE== True:
   print("Es mayor de edad")
   print("Puedes ir a jugar lol")
else:
    print("Eres menor de edad")
    print("Puedes ir a jugar micraf")
print("fin del programa")
