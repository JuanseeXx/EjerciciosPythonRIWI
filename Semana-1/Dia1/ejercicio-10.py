#Pide un número al usuario. Di si está dentro del rango de 1 a 10 (inclusive).
numeroUsuario = int(input("Ingresa un número para validar si está dentro del rango: "))

if numeroUsuario >= 1 and numeroUsuario <= 10:
    print(f"El número {numeroUsuario} está dentro del rango")
else:
    print(f"El número {numeroUsuario} está fuera del rango.")
