#Pide una contraseña al usuario. Si coincide con "python123", 
#imprime "Acceso concedido", de lo contrario, "Contraseña incorrecta".

password = "python123"
passwordInput = input("Ingrese la contraseña: ")

if passwordInput == password:
    print("Acceso concedido")
else:
    print("Contraseña incorrecta")