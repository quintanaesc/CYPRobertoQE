A=int(input("Introduce un entero positivo: "))
B=int(input("Introduce otro calor entero positivo: "))
C=int(input("Introduce un ultimo valor positivo:"))
if A>B:
    if A>C:
        print(f"A es el mayor con valor a {A}")
    elif A==C:
        print(f"A y C son iguales a {A} y son los mayores")
    else:
        print(f"C que vale {C} es el mayor")
elif  A==B:
    if A>C:
        print(f"A y B son los mayores con valor {B}")
    elif A==C:
        print(f"A, B, y C son iguales con un valor de {A}")
    else:
        print(f"C es el mayor que vale {C}")
elif B>C:
    print(f"B que vale {B} es el mayor")
elif B==C:
    print(f"B y C son los mayores con valor {B}")
else:
    print(f"C es el mayor con valor de {C}")

print("fin del programa")

