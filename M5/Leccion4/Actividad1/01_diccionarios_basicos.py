# Introducción a los diccionarios en Python
estudiantes = {
    "Ana": 5.5,
    "Luis": 6.2,
    "Carlos": 4.9
}

# Acceso a elementos
print("Nota de Ana:", estudiantes["Ana"])

# Agregar un nuevo estudiante
estudiantes["Javiera"] = 6.8

# Recorrer diccionario
for nombre, nota in estudiantes.items():
    print(f"{nombre}: {nota}")
