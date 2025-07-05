# Simulación básica de autenticación

usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

if usuario == "admin" and contrasena == "toor":
    print("Acceso concedido")
elif usuario == "admin":
    print("Contraseña incorrecta")
else:
    print("Usuario no reconocido")
