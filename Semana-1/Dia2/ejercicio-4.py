#Pide al usuario su edad.
#Si la edad es menor que 0 o mayor que 120, imprime "Edad no válida".
#Si está en el rango correcto, imprime "Edad válida".

edad = int(input("Ingrese su edad: "))

if edad < 0 or edad > 120:
    print("Edad no válida.")
else:
    print("Edad válida.")
