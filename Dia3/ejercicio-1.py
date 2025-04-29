biblioteca = {
    '001': {'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'año': 1967},
    '002': {'titulo': '1984', 'autor': 'George Orwell', 'año': 1949},
    '003': {'titulo': 'Orgullo y prejuicio', 'autor': 'Jane Austen', 'año': 1813},
    '004': {'titulo': 'Don Quijote de la Mancha', 'autor': 'Miguel de Cervantes', 'año': 1605},
    '005': {'titulo': 'El nombre de la rosa', 'autor': 'Umberto Eco', 'año': 1980}
}

def crear_libro():
    id_libro = input("Ingrese el ID del libro: ")
    if id_libro in biblioteca:
        print("Este ID ya existe. Intente con otro.")
        return
    
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    try:
        año = int(input("Ingrese el año de publicación del libro: "))
    except ValueError:
        print("El año debe ser un número entero.")
        return
    
    biblioteca[id_libro] = {'titulo': titulo, 'autor': autor, 'año': año}
    print("Libro agregado exitosamente.")

def leer_libros():
    if not biblioteca:
        print("No hay libros en la biblioteca.")
        return
    print("\nListado de libros: ")
    for id_libros, info in biblioteca.items():
        print(f"ID: {id_libros}, Titulo: {info['titulo']}, Autor: {info['autor']}, Año: {info['año']}")

def buscar_libro():
    criterio = input("¿Buscar por ID o por título? (escriba 'id' o 'titulo'): ").strip().lower()

    if criterio == 'id':
        id_buscar = input("Ingrese el ID del libro: ")
        libro = biblioteca.get(id_buscar)
        if libro:
            print(f"Titulo: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año']} ")
        else:
            print("Libro no encontrado.")
    elif criterio == 'titulo':
        titulo_buscar = input("Ingrese el título del libro: ").strip().lower()
        encontrado = False
        for info in biblioteca.values():
            if info['titulo'].lower() == titulo_buscar:
                print(f"Titulo: {info['titulo']}, Autor: {info['autor']}, Año{info['año']}")
                encontrado = True
                break
        if not encontrado:
            print("Libro no encontrado.")
    else:
        print("Opción no válida.")

def actualizar_libro():
    id_libro = input("Ingrese el ID del libro a actualizar: ")
    if id_libro not in biblioteca:
        print("No existe un libro con ese ID.")
        return

    print("¿Que desea actualizar?")
    print("1. Título")
    print("2. Autor")
    print("3. Año de publicación")
    opcion = input("Elija una de las opciones (1, 2 o 3): ")

    if opcion == '1':
        nuevo_titulo = input("Ingrese el nuevo título: ")
        biblioteca[id_libro]['titulo'] = nuevo_titulo
    elif opcion == '2':
        nuevo_autor = input("Ingrese el nuevo autor: ")
        biblioteca[id_libro]['autor'] = nuevo_autor
    elif opcion == '3':
        try:
            new_year = int(input("Ingrese el nuevo año de publicación: "))
            biblioteca[id_libro]['año'] = new_year
        except ValueError:
            print("El año debe ser un número entero.")
            return
    else:
        print("Opción no válida.")
        return

    print("Libro actualizado exitosamente.")

def eliminar_libro():
    id_libro = input("Ingrese el ID del libro a actualizar: ")
    if id_libro in biblioteca:
        del biblioteca[id_libro]
        print("Libro eliminado exitosamente.")
    else:
        print("No existe un libro con ese ID.")

def menu():
    while True:
        print("\n----------Gestión de Biblioteca----------")
        print("1. Agregar libro.")
        print("2. Mostrar todos los libros.")
        print("3. Buscar libro.")
        print("4. Actualizar un libro.")
        print("5. Eliminar un libro.")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            crear_libro()
        elif opcion == '2':
            leer_libros()
        elif opcion == '3':
            buscar_libro()
        elif opcion == '4':
            actualizar_libro()
        elif opcion == '5':
            eliminar_libro()
        elif opcion == '6':
            print("¡Hasta luego!")
        else:
            print("Opción no válida. Intente de nuevo.")

menu()