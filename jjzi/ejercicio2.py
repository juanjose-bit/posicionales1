placa1 = input("Ingrese la placa del primer bus: ")
pasajeros1 = int(input("Ingrese el número de pasajeros transportados por el primer bus: "))
valor_pasaje1 = float(input("Ingrese el valor del pasaje del primer bus: "))


placa2 = input("Ingrese la placa del segundo bus: ")
pasajeros2 = int(input("Ingrese el número de pasajeros transportados por el segundo bus: "))
valor_pasaje2 = float(input("Ingrese el valor del pasaje del segundo bus: "))


dinero1 = pasajeros1 * valor_pasaje1
dinero2 = pasajeros2 * valor_pasaje2


if dinero1 > dinero2:
    print("El bus que más dinero recogió fue:", placa1)
elif dinero2 > dinero1:
    print("El bus que más dinero recogió fue:", placa2)
else:
    print("Ambos buses recogieron la misma cantidad de dinero.")
