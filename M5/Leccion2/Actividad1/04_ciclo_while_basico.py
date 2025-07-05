# Ingresar nombres hasta que el usuario escriba 'fin'
print("Escribe nombres. Para salir, escribe 'fin'.")

nombre = ""
while nombre != "fin":
    nombre = input("Nombre: ")
    if nombre != "fin":
        print("Hola,", nombre)
