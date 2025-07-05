# Leer nombres hasta que se escriba 'fin'

print("Escribe nombres (escribe 'fin' para terminar):")

nombre = ""
while nombre != "fin":
    nombre = input("Nombre: ")
    if nombre != "fin":
        print(f"Estudiante registrado: {nombre}")
