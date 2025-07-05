# Clasificador de Edad
# Este programa solicita la edad del usuario y clasifica a la persona según su rango etario.

# Solicita la edad al usuario como entrada de texto
entrada = input("¿Cuántos años tienes? ")

# Convierte la entrada a entero (tipo int)
edad = int(entrada)

# Clasifica y muestra el resultado usando condiciones
if edad < 13:
    print("Eres un niño/a")
elif 13 <= edad <= 17:
    print("Eres un adolescente")
else:
    print("Eres un adulto")
