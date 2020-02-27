A=int(input("Incerte un primer numero: "))
B=int(input("Incerte un segundo numero: "))
C=int(input("Incerte un tercer numero: "))
if B>A:
    if C>B:
        print(f"Los numeros {A}, {B} y {C} estan ordenados de modo cresiente")
    else:
        print(f"Los numeros {A}, {B} y {C} no estan ordenados de modo cresiente")
else:
    print(f"Los numeros {A}, {B} y {C} no estan ordenados de modo cresiente")
print("fin del programa")

