import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Datos de ejemplo
usuarios = [
    ("María Pérez", "maria.perez@example.com", "Analista"),
    ("Juan González", "juan.gonzalez@example.com", "Pentester"),
    ("Ana Torres", "ana.torres@example.com", "Auditor"),
    ("Carlos Soto", "carlos.soto@example.com", "Administrador")
]

# Insertar los datos
cursor.executemany('INSERT INTO usuarios (nombre, correo, rol) VALUES (?, ?, ?)', usuarios)

conn.commit()
conn.close()

print("Datos insertados con éxito.")
