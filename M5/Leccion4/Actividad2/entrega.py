# Descripción: Genera saludos personalizados para una lista de nombres utilizando un bucle for.

# Lista de nombres
nombres = ["Ana", "Luis", "Camila", "Diego"]

# Recorre la lista y muestra un saludo para cada persona
for nombre in nombres:
    if nombre.endswith("a"):
        print(f"Hola, {nombre}. ¡Bienvenida a Python!")
    else:
        print(f"Hola, {nombre}. ¡Bienvenido a Python!")
