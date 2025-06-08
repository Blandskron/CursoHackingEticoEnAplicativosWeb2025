import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Recuperar los datos
cursor.execute('SELECT * FROM usuarios')
datos = cursor.fetchall()

# Imprimir los registros
print("Registros en la base de datos:")
for usuario in datos:
    print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Correo: {usuario[2]}, Rol: {usuario[3]}")

conn.close()
