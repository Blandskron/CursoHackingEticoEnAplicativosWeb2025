def registrar_estudiantes():
    estudiantes = {}
    while True:
        nombre = input("Ingrese el nombre del estudiante (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        try:
            nota = float(input(f"Ingrese la nota final de {nombre}: "))
            estudiantes[nombre] = nota
        except ValueError:
            print("Error: La nota debe ser un número. Inténtalo de nuevo.")
    return estudiantes

def calcular_promedio(estudiantes):
    if len(estudiantes) == 0:
        return 0
    return sum(estudiantes.values()) / len(estudiantes)

def clasificar_estudiantes(estudiantes):
    aprobados = []
    reprobados = []
    for nombre, nota in estudiantes.items():
        if nota >= 6.0:
            aprobados.append(nombre)
        else:
            reprobados.append(nombre)
    return aprobados, reprobados

def mostrar_resultados(estudiantes):
    promedio = calcular_promedio(estudiantes)
    aprobados, reprobados = clasificar_estudiantes(estudiantes)

    print("\nResultados:")
    print(f"Total de estudiantes: {len(estudiantes)}")
    print(f"Aprobados: {len(aprobados)}")
    print(f"Reprobados: {len(reprobados)}")
    print(f"Promedio general: {promedio:.2f}")
    
    print("\nEstudiantes que aprobaron:")
    for nombre in aprobados:
        print(f"- {nombre}")

if __name__ == "__main__":
    print("Registro de Estudiantes")
    estudiantes = registrar_estudiantes()
    mostrar_resultados(estudiantes)
