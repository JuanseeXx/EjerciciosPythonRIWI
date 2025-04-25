#Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. 
# Di si su número es mayor, menor o igual al número secreto.

numeroSecreto = 7
numeroUsuario = int(input("Ingrese el número que usted crea que es el número secreto: "))

if numeroUsuario > numeroSecreto:
    print("Tu número es mayor.")
elif numeroUsuario < numeroSecreto:
    print("Tu número es menor.")
else:
    print("ADIVINASTE!!")