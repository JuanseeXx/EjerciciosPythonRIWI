#Pide al usuario el total de una cuenta. Luego pregunta 
#qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y 
#muestra el valor de la propina.

totalAccount = float(input("Ingrese el total de la cuenta: "))
propinaOtorgada = int(input("Que porcentaje de propina quieres dejar? (10, 15, 20): "))
porcentajeDePropina = [10, 15, 20]
totalPropina = 0

if propinaOtorgada == porcentajeDePropina[0]:
    totalPropina = totalAccount * 10 / 100
elif propinaOtorgada == porcentajeDePropina[1]:
    totalPropina = totalAccount * 15 / 100
elif propinaOtorgada == porcentajeDePropina[2]:
    totalPropina = totalAccount * 20 / 100
else:
    print("Valor no valido. Por favor ingrese un porcentaje válido de propina (10,15 o 20): ")

print(f"La propina del {propinaOtorgada}% es: ${totalPropina:.2f}")
