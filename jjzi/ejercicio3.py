placa = input("Ingrese la placa del bus: ")
pasajeros = int(input("Ingrese el número de pasajeros transportados: "))
ruta = input("Ingrese la ruta donde prestó el servicio (A o B): ")

if ruta.upper() == "A":
    valor_pasaje = 1200
elif ruta.upper() == "B":
    valor_pasaje = 1000
else:
    print("Ruta inválida.")
    valor_pasaje = 0


dinero = pasajeros * valor_pasaje


if valor_pasaje > 0:
    print("El bus con placa", placa, "recolectó $", dinero)
