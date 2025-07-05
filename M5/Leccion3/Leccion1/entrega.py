# Función que evalúa si un estudiante aprueba o reprueba
def evaluar_estudiante(nombre, promedio):
    if promedio >= 6.0:
        print(f"{nombre} ha aprobado con promedio {promedio}")
        return True
    else:
        print(f"{nombre} ha reprobado con promedio {promedio}")
        return False

# Programa principal
print("🎓 Evaluador de Estudiantes")
print("Escribe 'fin' como nombre para terminar.")

# Inicialización de contadores
total_estudiantes = 0
aprobados = 0
reprobados = 0

while True:
    nombre = input("\nNombre del estudiante: ")
    if nombre.lower() == "fin":
        break

    try:
        promedio = float(input("Promedio final del estudiante: "))
    except ValueError:
        print("Promedio inválido. Debe ser un número.")
        continue

    total_estudiantes += 1
    if evaluar_estudiante(nombre, promedio):
        aprobados += 1
    else:
        reprobados += 1

# Resumen final
print("\nResumen Final:")
print("Total de estudiantes evaluados:", total_estudiantes)
print("Cantidad de aprobados:", aprobados)
print("Cantidad de reprobados:", reprobados)
