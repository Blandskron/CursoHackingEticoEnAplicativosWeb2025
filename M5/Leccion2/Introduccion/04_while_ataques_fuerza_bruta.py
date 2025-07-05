# Simulación básica de fuerza bruta limitada a 3 intentos

clave_real = "supersegura"
intentos = 0

while intentos < 3:
    clave_ingresada = input("Introduce la clave: ")
    if clave_ingresada == clave_real:
        print("Acceso autorizado")
        break
    else:
        print("Clave incorrecta")
        intentos += 1

if intentos == 3:
    print("Demasiados intentos. Sistema bloqueado")
