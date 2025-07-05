# Calculadora de Área de un Rectángulo

# Definición de la función que calcula el área
def calcular_area(ancho, alto):
    area = ancho * alto
    return area

# Programa principal
print("Calculadora de Área de un Rectángulo")

# Solicitar datos al usuario
try:
    ancho = float(input("Ingrese el ancho: "))
    alto = float(input("Ingrese el alto: "))

    # Calcular el área usando la función
    resultado = calcular_area(ancho, alto)

    # Mostrar el resultado
    print(f"\nEl área del rectángulo es: {resultado}")
except ValueError:
    print("Error: Debes ingresar valores numéricos válidos.")
