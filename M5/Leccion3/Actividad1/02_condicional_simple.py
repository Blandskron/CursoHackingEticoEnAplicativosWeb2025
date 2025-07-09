# Evaluar si una nota aprueba o reprueba

nota = float(input("Ingresa tu nota final: "))

if nota >= 6.0:
    print("Aprobado")
elif nota >= 5.0:
    print("Aprobado con condiciones")
else:
    print("Reprobado")

nota = float(input("Ingresa tu nota final: "))

if nota >= 6.0:
    print("✅ Aprobado con buen rendimiento")
elif nota >= 5.0:
    if nota >= 5.5:
        print("⚠️ Aprobado con condiciones: debe reforzar contenidos")
    else:
        print("⚠️ Aprobado raspando: revisión con profesor")
else:
    if nota >= 4.0:
        print("❌ Reprobado: puede apelar")
    else:
        print("❌ Reprobado directamente: sin posibilidad de apelación")
