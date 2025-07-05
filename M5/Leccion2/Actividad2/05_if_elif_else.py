# Clasificar temperatura según su valor

temperatura = int(input("Ingresa la temperatura en grados Celsius: "))

if temperatura < 10:
    print("Hace mucho frío.")
elif temperatura < 25:
    print("El clima está templado.")
else:
    print("Hace calor.")
