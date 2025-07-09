# -------------------------------
# LISTA (list) - mutable, ordenada
# -------------------------------
print("📌 Lista")

frutas = ["manzana",  "pera", "naranja", "kiwi"]
frutas.append("kiwi")           # Agrega al final
frutas.insert(1, "pera")        # Inserta en posición 1
frutas.remove("banana")         # Elimina por valor
frutas.sort()                   # Ordena
frutas.reverse()                # Invierte el orden

print("Lista final:", frutas)
print("Índice de 'naranja':", frutas.index("naranja"))

# -------------------------------
# TUPLA (tuple) - inmutable, ordenada
# -------------------------------
print("\n📌 Tupla")

colores = ("rojo", "verde", "azul", "rojo")
print("Tupla:", colores)
print("Cantidad de 'rojo':", colores.count("rojo"))
print("Índice de 'verde':", colores.index("verde"))

# -------------------------------
# CONJUNTO (set) - sin orden, sin duplicados
# -------------------------------
print("\n📌 Conjunto (set)")

numeros = {1, 2, 3, 4}
numeros.add(5)              # Agrega un elemento
numeros.discard(2)          # Elimina si existe
numeros.update({6, 7, 3})   # Agrega múltiples elementos
otros = {3, 7, 8}

print("Unión:", numeros.union(otros))
print("Intersección:", numeros.intersection(otros))
print("Diferencia:", numeros.difference(otros))
print("Diferencia:", otros.difference(numeros))

# -------------------------------
# DICCIONARIO (dict) - clave-valor, mutable
# -------------------------------
print("\n📌 Diccionario")

persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Santiago"
}

persona["profesion"] = "Ingeniera"     # Agrega clave
persona["edad"] = 31                   # Modifica valor
del persona["ciudad"]                  # Elimina clave
valor = persona.get("pais", "Chile")  # Valor con default

print("Diccionario:", persona)
print("Claves:", list(persona.keys()))
print("Valores:", list(persona.values()))
print("Items:", list(persona.items()))
print("País:", valor)
