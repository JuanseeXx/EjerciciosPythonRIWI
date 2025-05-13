#Pide tres números al usuario.
#Usa condicionales (if) para decir cuál es el más pequeño.

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

if numero1 <= numero2 and numero1 <= numero3:
    print(f"El número {numero1} es el menor.")
elif numero2 <= numero1 and numero2 <= numero3:
    print(f"El número {numero2} es el menor.")
else:
    print(f"El número {numero3} es menor.")