ARSU=0
ARNO=0
MERSU=50000
ARCE=0
for I in range(1,13,1):
    print("Mes", I)
    RNO=float(input("Promedio de lluvia e el mes, en la region norte: "))
    RCE=float(input("Promedio de lluvia e el mes, en la region centro: "))
    RSU=float(input("Promedio de lluvia e el mes, en la region sur: "))

    ARNO+=RNO
    ARCE+=RCE
    ARSU+=RSU

    if RSU<MERSU:
        MERSU=ARSU
        MES=I
PRORCE=ARCE/12
print(f"El promedio de la region centro es: {PRORCE}")
print(f"El mes con menor lluvia en la region sur es: {MES}")
print(f"El registro del mes con menor lluvia es: {MERSU}")
if ARNO>ARCE:
    if ARNO>ARSU:
        print("La region con menor lluvia es la region norte")
    else:
        print("La region con menor lluvia es la region sur")
else:
    if ARCE>ARSU:
        print("La region con mayor lluvia es la region centro")
    else:
        print("La region con mayor lluvia es la region sur")
print("fin del programa")
