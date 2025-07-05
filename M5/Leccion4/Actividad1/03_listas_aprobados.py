# Clasificación de estudiantes según su nota
estudiantes = {
    "Ana": 5.5,
    "Luis": 6.2,
    "Carlos": 4.9,
    "Javiera": 7.0
}

aprobados = []
reprobados = []

for nombre, nota in estudiantes.items():
    if nota >= 6.0:
        aprobados.append(nombre)
    else:
        reprobados.append(nombre)

print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
