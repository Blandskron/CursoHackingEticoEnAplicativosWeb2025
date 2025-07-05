# Recolección de datos del usuario en un diccionario
estudiantes = {}

while True:
    nombre = input("Nombre del estudiante (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    try:
        nota = float(input(f"Ingrese nota de {nombre}: "))
        estudiantes[nombre] = nota
    except ValueError:
        print("Entrada inválida. Intente nuevamente.")

print("Datos ingresados:")
print(estudiantes)
