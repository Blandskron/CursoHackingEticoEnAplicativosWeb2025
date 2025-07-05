# Calculadora de Promedios
# Este programa permite ingresar notas indefinidamente hasta que el usuario escriba 'fin'.
# Luego muestra el promedio general, cantidad de aprobados y reprobados.

print("Calculadora de Promedios")
print("Ingresa las notas de los estudiantes (escribe 'fin' para terminar):")

# Inicialización de variables acumuladoras
suma_notas = 0.0
total_estudiantes = 0
aprobados = 0
reprobados = 0

while True:
    entrada = input("Nota del estudiante: ")
    
    if entrada.lower() == "fin":
        break

    try:
        nota = float(entrada)
        
        if nota < 0 or nota > 10:
            print("La nota debe estar entre 0 y 10. Intenta nuevamente.")
            continue
        
        suma_notas += nota
        total_estudiantes += 1

        if nota >= 6.0:
            aprobados += 1
        else:
            reprobados += 1

    except ValueError:
        print("Entrada inválida. Por favor ingresa un número o 'fin'.")

# Resultados finales
if total_estudiantes > 0:
    promedio = suma_notas / total_estudiantes
    print("\nResultados:")
    print(f"Promedio general: {promedio:.2f}")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")
    print(f"Total de estudiantes: {total_estudiantes}")
else:
    print("\nNo se ingresaron notas válidas.")
