#Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si 
# también es divisible entre 400).

yearUser = int(input("Ingresa un año (Sin puntos ni comas): "))

if (yearUser % 4 == 0 and yearUser % 100 != 0) or (yearUser % 400 == 0):
    print(f"El año {yearUser} es bisiesto")
else:
    print(f"El año {yearUser} no es bisiesto")