# Este script permite ingresar nombres desde teclado y almacenarlos en una lista.

nombres = []

print("Introduce 3 nombres:")
for _ in range(3):
    nombre = input("Nombre: ")
    nombres.append(nombre)

print("Nombres ingresados:", nombres)
