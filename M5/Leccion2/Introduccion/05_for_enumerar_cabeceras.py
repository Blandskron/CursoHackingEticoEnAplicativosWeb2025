# Enumerar cabeceras HTTP como ejemplo de extracción de datos

cabeceras = ["Content-Type", "Server", "X-Powered-By", "Content-Length"]

print("Cabeceras comunes encontradas en un servidor:")

for cabecera in cabeceras:
    print("- " + cabecera)
