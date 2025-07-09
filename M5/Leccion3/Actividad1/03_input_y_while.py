# Leer nombres hasta que se escriba 'fin'

print("Escribe nombres (escribe 'fin' para terminar):")

nombre = ""
while nombre != "fin":
    nombre = input("Nombre: ")
    if nombre != "fin":
        print(f"Estudiante registrado: {nombre}")


print("Escribe nombres de estudiantes (escribe 'fin' para terminar):")

nombre = ""
while nombre != "fin":
    nombre = input("Nombre: ")
    if nombre == "fin":
        break
    
    nota = ""
    while not nota.replace(".", "").isdigit():
        nota = input(f"Ingrese nota de {nombre}: ")
    
    print(f"Estudiante: {nombre} | Nota: {nota}")
