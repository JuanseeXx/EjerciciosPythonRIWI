#Nivel básico:

#1.Saludo personalizado
#Crea una función que reciba un nombre y muestre un saludo personalizado.
def saludo():
    nombre = input("Ingresa tu nombre: ")
    print(f"¡Bienvenido, {nombre}!")

#2.Suma de dos números
#Escribe una función que reciba dos números y devuelva su suma.
def suma():
    num1 = int(input("Ingresa un número: "))
    num2 = int(input("Ingresa otro número: "))
    sum = num1 + num2
    print(f"La suma de los dos números da un total de {sum}")

#3.Número par o impar
#Crea una función que determine si un número es par o impar.
def parImpar():
    numero = int(input("Ingresa un número para saber si es par o impar: "))
    if numero % 2 == 0:
        print(f"El número {numero}, es un número par.")
    else:
        print(f"El número {numero}, es un número impar.")

#4.Mayoría de edad
#Escribe una función que reciba una edad y devuelva si es mayor o menor de edad.
def mayorEdad():
    edad = int(input("Ingresa tu edad: "))
    if edad > 17:
        print("Eres mayor de edad.")
    else:
        print("Aún eres menor de edad.")

#5.Conversor de temperatura
#Crea una función que convierta grados Celsius a Fahrenheit.
def celsiusFahrenheit():
    temperaturaCelsius = float(input("Ingresa la temperatura actual (°C): "))
    temperaturaFahrenheit = temperaturaCelsius * 1.8 + 32
    print(f"Temperatura {temperaturaCelsius:.1f}°C en Fahrenheit es de {temperaturaFahrenheit:.1f}°F")
    
#6.Área de un triángulo
#Escribe una función que devuelva el área de un triángulo dado su base y altura.
def areaTriangulo():
    base = float(input("Dame la base de un triángulo (en cm, ej: '8.5'): "))
    altura = float(input("Dame la altura del triángulo: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es de {area}cm²")


#7.Mayor de una lista
#Crea una función que reciba una lista de números y devuelva el mayor.
def listaNumeros():
    listaUser = input("Ingresa una lista de números separados por coma: ")
    lista = [int(num.strip()) for num in listaUser.split(',')]
    mayor = max(lista)
    print(f"El número mayor es: {mayor}")
    
#8.Contar letras
#Escribe una función que cuente cuántas veces aparece una letra en una palabra.
def contarLetras():
    palabra = input("Ingrese una palabra: ").strip().lower()
    letraContar = input("Que letra de su palabra desea contar cuantas veces aparece: ").strip().lower()
    count = palabra.count(letraContar)
    
    print(f"La letra '{letraContar}', aparece {count} veces en la palabra '{palabra}'")
    
#Nivel Intermedio:

#9.Filtrar pares
#Crea una función que reciba una lista de números y devuelva solo los pares.
def filtrarPares():
     listaUser = input("Ingresa una lista de números separados por coma: ")
     numeros = [int(num.strip()) for num in listaUser.split(',')]
     numerosPares = [num for num in numeros if num % 2 == 0]
     print(f"Números pares: {numerosPares}")

#10.Palíndromo
#Escribe una función que determine si un texto es un palíndromo.
def textoPalíndromo():
    texto = input("Escribe un texto para determinar si es palíndromo: ").lower().strip()
    if texto == texto[::-1]:
        print("Es palíndromo.")
    else:
        print("No es palíndromo.")
    
#11.Factorial
#Crea una función que calcule el factorial de un número entero positivo.
def factorialNumero():
    num = int(input("Ingresa un número para calcular su factorial: "))
    resultado = 1
    for i in range (1, num + 1):
        resultado *= i
    print(resultado)


#12.Eliminar duplicados
#Escribe una función que reciba una lista y devuelva una nueva sin elementos repetidos.
def listaSinRepetidos():
    listaUser = input("Ingresa una lista de números separados por coma: ")
    lista = listaUser.split(',')
    lista = [elemento.strip() for elemento in lista]
    nueva_lista = []
    vistos = set()
    for elemento in lista:
        if elemento not in vistos:
            nueva_lista.append(elemento)
            vistos.add(elemento)
    print("Lista sin elementos repetidos: ", nueva_lista)

#13.FizzBuzz
#Crea una función que reciba un número y devuelva "Fizz", "Buzz" o "FizzBuzz" según las reglas del juego.
def FizzBuzz():
    num = int(input("Ingresa un número: "))
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#14.Contar vocales
#Escribe una función que reciba una cadena y devuelva la cantidad de vocales.
def cadenaVocales():
    cadena = input("Ingrese un texto para contar sus vocales: ")
    contador = 0
    for letra in cadena.lower():
        if letra in 'aeiou':
            contador += 1
    print("Cantidad de vocales: ", contador)

#15.Invertir texto
#Crea una función que invierta una cadena de texto
def invertirTexto():
    texto = input("Ingrese el texto que desea invertir: ").lower()
    textoInverso = texto[::-1].lower()
    print(textoInverso)


#Nivel avanzado:

#16.Validar contraseña segura
#Escribe una función que valide si una contraseña cumple con requisitos de seguridad (mayúsculas, minúsculas, números y símbolos).
def validarContraseña():
    contraseña = input("Ingrese una contraseña: ")
    
    tiene_mayusculas = False
    tiene_minusculas = False
    tiene_numeros = False
    tiene_simbolos = False
    
    for c in contraseña:
        if c.isupper():
            tiene_mayusculas = True
        elif c.islower():
            tiene_minusculas = True
        elif c.isdigit():
            tiene_numeros = True
        elif not c.isalnum():
            tiene_simbolos = True
            
    if tiene_mayusculas and tiene_minusculas and tiene_numeros and tiene_simbolos:
        print("Contraseña segura.")
    else:
        print("Contraseña insegura. Aegurate de incluir mayúsculas, minúsculas, números y símbolos")

#17.Simular dado
#Crea una función que simule el lanzamiento de un dado de 6 caras.
def lanzarDado():
    import random
    return random.randint(1, 6)
    

#18.Suma de elementos únicos
#Escribe una función que reciba una lista de números y devuelva la suma de los elementos únicos.
def sumaElementosUnicos():
    lista = input("Ingresa una lista de números separados por espacios: ").split()
    lista = [int(x) for x in lista]
    suma = 0
    for numero in lista:
        if lista.count(numero) == 1:
            suma += numero
    print(suma)


#19.Generador de contraseñas
#Crea una función que genere una contraseña aleatoria de una longitud dada.
def crearContraseña():
    import string
    import random
    longitud = int(input("Introduce la longitud de la contraseña: "))
    contraseña = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(longitud))
    print("Contraseña generada: " + contraseña)

#20.Composición de funciones
#Escribe una función que reciba otra función como parámetro y aplique una composición de funciones
def multiplicar_por_dos(x):
    return x * 2

def sumar_uno(x):
    return x + 1

def aplicar_composicion(multiplicar_por_dos, sumar_uno, valor):
    return multiplicar_por_dos(sumar_uno(valor))

resultado = aplicar_composicion(sumar_uno, multiplicar_por_dos, 10)
print(resultado)