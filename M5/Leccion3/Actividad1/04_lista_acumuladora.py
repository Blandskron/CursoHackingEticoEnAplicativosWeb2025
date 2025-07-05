# Acumular nombres en una lista

nombres = []

for i in range(3):
    nombre = input(f"Ingrese nombre del estudiante #{i+1}: ")
    nombres.append(nombre)

print("Lista de estudiantes registrados:")
for nombre in nombres:
    print("-", nombre)
