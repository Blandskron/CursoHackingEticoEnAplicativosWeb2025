import sqlite3

conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT NOT NULL,
        rol TEXT NOT NULL
    )
''')

usuarios = [
    ("Laura Méndez", "laura@example.com", "Pentester"),
    ("Marco Díaz", "marco@example.com", "Analista"),
    ("Ana Jiménez", "ana@example.com", "Auditor"),
    ("Luis Rojas", "luis@example.com", "Administrador")
]

cursor.executemany("INSERT INTO usuarios (nombre, correo, rol) VALUES (?, ?, ?)", usuarios)

conn.commit()
conn.close()

print("Base de datos creada y poblada.")
