# Cálculo del promedio de notas
estudiantes = {
    "Ana": 5.5,
    "Luis": 6.2,
    "Carlos": 4.9,
    "Javiera": 7.0
}

suma_notas = sum(estudiantes.values())
cantidad = len(estudiantes)
promedio = suma_notas / cantidad if cantidad > 0 else 0

print(f"Promedio general: {promedio:.2f}")
