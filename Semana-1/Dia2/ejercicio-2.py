#Crea una lista con 5 números.
#Pide un número al usuario y verifica si está en la lista usando in.

numeros = [3, 7, 9, 15, 19]
numeroUsuario = int(input("Ingrese un número para ver si está en la lista: "))

if numeroUsuario in numeros:
    print("Tu número está en la lista")
else:
    print("Tu número no está en la lista")