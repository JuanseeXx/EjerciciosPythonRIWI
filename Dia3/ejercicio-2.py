agenda = {}

def agregar_contacto(nombre, telefono, email):
    nombre = nombre.lower()
    if nombre in agenda:
        print(f"El contacto {nombre} ya existe en la lista. Intenta con otro nombre.")
    else:
        agenda[nombre] = {'telefono': telefono, 'email': email}
        print(f"El contacto '{nombre}' fue añadido exitosamente.")

def listar_contactos():
    if not agenda:
        print("La agenda está vacia.")
    else:
        for nombre, datos in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {datos['telefono']}, Email: {datos['email']}")

def buscar_contactos(nombre):
    nombre = nombre.lower()
    if nombre in agenda:
        datos = agenda[nombre]
        print(f"Nombre: {nombre}, Teléfono: {datos['telefono']}, Email: {datos['email']}")
    else:
        print(f"El contacto '{nombre}' no se encuentra en la agenda.")

def actualizar_contacto(nombre):
    nombre = nombre.lower()
    if nombre in agenda:
        print(f"\nContacto encontrado: {nombre}")
        print(f"Telefono actual: {agenda[nombre]['telefono']}")
        print(f"Email actual: {agenda[nombre]['email']}")
        nuevo_telefono = input("Nuevo teléfono (deja en blanco si no deseas cambiarlo): ")
        nuevo_email = input("Nuevo email (deja en blanco si no deseas cambiarlo): ")
        if nuevo_telefono != "":
            agenda[nombre]["telefono"] = nuevo_telefono
        if nuevo_email != "":
            agenda[nombre]["email"] = nuevo_email
        print(f"Contacto '{nombre}' actualizado correctamente.")
    else:
        print(f"El contacto '{nombre}' no se encuentra en la agenda.")

def eliminar_contacto(nombre):
    nombre = nombre.lower()
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto '{nombre}' fue eliminado exitosamente.")
    else:
        print(f"El contacto '{nombre}' no existe en la agenda")

def menu():
        print("\n----------Gestión de Agenda----------")
        print("1. Agregar contacto.")
        print("2. Listar contactos.")
        print("3. Buscar contacto por nombre.")
        print("4. Actualizar contacto.")
        print("5. Eliminar contacto.")
        print("6. Salir")

while True:
    menu()
    opcion = input("\nSeleccione una opción (1-6): ")

    if opcion == '1':
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        agregar_contacto(nombre, telefono, email)
    elif opcion == '2':
        listar_contactos()
    elif opcion == '3':
        nombre = input("Nombre del contacto a buscar: ")
        buscar_contactos(nombre)
    elif opcion == '4':
        nombre = input("Nombre del contacto a actualizar: ")
        actualizar_contacto(nombre)
    elif opcion == '5':
        nombre = input("Nombre del contacto a eliminar: ")
        eliminar_contacto(nombre)
    elif opcion == '6':
        print("Saliendo de la agenda...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")