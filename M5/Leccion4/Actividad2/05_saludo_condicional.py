# Este script usa condicionales para adaptar el saludo según el género (de forma básica).

nombres = ["Ana", "Luis", "Camila", "Diego"]

for nombre in nombres:
    if nombre.endswith("a"):
        print(f"Hola, {nombre}. ¡Bienvenida a Python!")
    else:
        print(f"Hola, {nombre}. ¡Bienvenido a Python!")
