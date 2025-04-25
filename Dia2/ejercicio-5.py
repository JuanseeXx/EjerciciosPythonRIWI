#Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
#Pide al usuario su nombre.
#Usa if para decir si está en la lista de invitados o no.

nombres = ["Ana", "Luis", "Sofia"]

nombreUsuario = input("Ingrese su nombre: ")

if nombreUsuario.lower() in [nombre.lower() for nombre in nombres]:
    print("Estás en la lista de invitados.")
else:
    print("No estás en la lista de invitados.")