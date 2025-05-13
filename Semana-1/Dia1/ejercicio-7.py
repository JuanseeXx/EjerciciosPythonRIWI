#Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.

numero1 = int(input("Dame el primer número: "))
numero2 = int(input("Dame el segundo número: "))

if numero1 > numero2:
    print(f"El número {numero1} es mayor.")
elif numero1 < numero2:
    print(f"El número {numero2} es mayor.")
else:
    print("Los dos números son iguales.")