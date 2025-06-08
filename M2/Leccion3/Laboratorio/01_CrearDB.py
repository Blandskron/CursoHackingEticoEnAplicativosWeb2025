import sqlite3

# Conexión y creación de la base de datos
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Crear la tabla usuarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT NOT NULL,
        rol TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

print("Base de datos y tabla creadas con éxito.")
