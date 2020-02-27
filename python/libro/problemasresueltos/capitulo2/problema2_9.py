PB=float(input("Ingrese el precio base del producto: $"))
if PB>500:
    IM=20*0.30+(PB-40)*0.50
elif PB>40:
    IM=20*0.30+(PB-40)*0.40
elif PB>20:
    IM=(PB-20)*0.30
else:
    IM=0
PF=PB+IM
print(f"El impuesto al producto es de ${IM} y su total a pagar es de ${PF}")
print("fin del programa")
