import datetime

compras = []
id_contador = 1

def generarId():
    global id_contador
    return f"COMP{id_contador:04d}"

def calcularPrecioBase(tipoViaje):
    if tipoViaje == 'nacional'.strip().lower():
        return 230000
    elif tipoViaje == 'internacional'.strip().lower():
        return 4200000
    else:
        return 0
    
def calcularCostoEquipajePrincipal(peso):
    if peso <= 20:
        return 50000
    elif peso <= 30:
        return 70000
    elif peso <= 50:
        return 110000
    else:
        return None
    
def estadoEquipajeMano(pesoMano):
    return "Aceptado" if pesoMano <= 13 else "Rechazado"

def registrarCompra():
    global id_contador
    print("\n----------NUEVA RESERVA----------")
    nombre = input("Nombre del pasajero: ")
    tipoViaje = input("Tipo de viaje (Nacional/Internacional): ").strip().lower()
    destino = "Bogotá → Medellín" if tipoViaje == 'nacional'.strip().lower() else "Bogotá → España".strip().lower()

    try:
        peso_principal = float(input("Ingrese el peso del equipaje principal (kg): "))
    except ValueError:
        print("Peso inválido.")
        return
    
    lleva_mano = input("¿Lleva equipaje de mano? (si/no): ").strip().lower()
    pesoMano = 0
    if lleva_mano == 'si'.lower():
        try:
            pesoMano = float(input("Peso del equipaje de mano (kg): "))
        except ValueError:
            print("Peso inválido.")
            return
    
    fecha = input("Fecha del viaje (YYYY-MM-DD): ")
    id_compra = generarId()
    id_contador += 1

    precio_base = calcularPrecioBase(tipoViaje)
    costo_equipaje = calcularCostoEquipajePrincipal(peso_principal)

    estado_principal = "Admitido" if costo_equipaje is not None else "No admitido (debe cancelar o viajar sin equipaje)"
    estado_mano = estadoEquipajeMano(pesoMano) if lleva_mano == 'si' else 'No lleva'

    total = precio_base + (costo_equipaje if costo_equipaje is not None else 0)

    compra = {
        "id": id_compra,
        "nombre": nombre,
        "tipoViaje": tipoViaje,
        "destino": destino,
        "fecha": fecha,
        "estado_principal": estado_principal,
        "estado_mano": estado_mano,
        "total": total
    }

    compras.append(compra)

    print("\n----------Resumen de la Compra----------")
    print(f"ID de compra: {id_compra}")
    print(f"Nombre: {nombre}")
    print(f"Destino: {destino}")
    print(f"Fecha: {fecha}")
    print(f"Estado del equipaje principal: {estado_principal}")
    print(f"Estado del equipaje de mano: {estado_mano}")
    print(f"Total a pagar: ${total:,}" if estado_principal == "Admitido" else "Total a pagar: $N/A")

def mostrarReporteAdmin():
    print("\n-----Reporte Administrativo-----")
    total_recaudo = sum(c["total"] for c in compras)
    total_pasajeros = len(compras)
    total_nacionales = sum(1 for c in compras if c["tipoViaje"] == "nacional")
    total_internacionales = sum(1 for c in compras if c["tipoViaje"] == "internacional")

    print(f"Total recaudado: ${total_recaudo:,}")
    print(f"Pasajeros procesados: {total_pasajeros}")
    print(f"Pasajeros nacionales: {total_nacionales}")
    print(f"Pasajeros internacionales: {total_internacionales}")

    fecha_busqueda = input("Ingresa fecha para consultar recaudación (YYYY-MM-DD): ")
    recaudo_fecha = sum(c["total"] for c in compras if c["fecha"] == fecha_busqueda and c["estado_principal"] == "Admitido")
    print(f"Total recaudado el {fecha_busqueda}: ${recaudo_fecha:,}")

    id_busqueda = input("Ingrese el ID de compra para consultar detalles (ej: COMP0001): ")
    compra = next((c for c in compras if c["id"] == id_busqueda), None)
    if compra:
        print("\n---Detalles de la compra---")
        for k, v in compra.items():
            print(f"{k.capitalize()}: {v}")
    else:
        print("Compra no encontrada.")

def menu():
    while True:
        print("\n-----Menú principal-----")
        print("1.Registrar nueva compra: ")
        print("2.Ver reporte administrativo")
        print("3.Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrarCompra()
        elif opcion == '2':
            mostrarReporteAdmin()
        elif opcion == '3':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

menu()