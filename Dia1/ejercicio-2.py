#Pide un número al usuario. Di si es positivo, negativo o si es cero.

numero = int(input("Ingrese un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero == 0:
    print("El número es 0")
else:
    print("El número es negativo.")