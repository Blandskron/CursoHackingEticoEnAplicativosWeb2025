# Uso de funciones para modularizar el programa

def registrar_estudiantes():
    datos = {}
    while True:
        nombre = input("Nombre del estudiante (o 'fin' para salir): ")
        if nombre.lower() == "fin":
            break
        try:
            nota = float(input("Nota final: "))
            datos[nombre] = nota
        except ValueError:
            print("Nota inválida. Intente nuevamente.")
    return datos

def mostrar_aprobados(estudiantes):
    for nombre, nota in estudiantes.items():
        if nota >= 6.0:
            print(f"{nombre} ha aprobado con nota {nota}")

estudiantes = registrar_estudiantes()
mostrar_aprobados(estudiantes)
