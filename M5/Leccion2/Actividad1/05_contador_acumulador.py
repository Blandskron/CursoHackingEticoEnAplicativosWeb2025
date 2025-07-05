# Acumulador y contador para calcular promedio
suma = 0
cantidad = 0

print("Ingresa 3 notas para calcular el promedio:")

while cantidad < 3:
    nota = float(input(f"Ingrese nota {cantidad + 1}: "))
    suma += nota
    cantidad += 1

promedio = suma / cantidad
print("Promedio final:", promedio)
