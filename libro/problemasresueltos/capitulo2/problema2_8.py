N=int(input("Ingrese el monto de compra: "))
if N<500:
    print(f"Su cuenta total es de {N}")
elif N<=1000:
    P=N-(N*0.05)
    print(f"Su cuenta total es de {P}")
elif N<=7000:
    P=N-(N*0.11)
    print(f"Su cuenta total es de {P}")
elif N<=15000:
    P=N-(N*0.18)
    print(f"Su cuenta total es de {P}")
else:
    P=N-(N*0.25)
    print(f"Su cuenta total es de {P}")
print("fin del programa")


