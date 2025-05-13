nombres = []

while True:
    nuevo_valor = input("Ingrese un nombre (o 'salir' para terminar): ")
    if nuevo_valor.lower() == 'salir':
        break
    nombres.insert(0, nuevo_valor)
    print("Lista actual: ", nombres)
