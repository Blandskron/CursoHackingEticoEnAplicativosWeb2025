from flask import Flask, render_template_string
import psycopg2

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Usuarios</title>
</head>
<body>
  <h1>Lista de Usuarios</h1>
  <ul>
    {% for nombre in nombres %}
      <li>{{ nombre }}</li>
    {% endfor %}
  </ul>
</body>
</html>
"""

@app.route('/')
def index():
    conn = psycopg2.connect(
        host="postgres",
        dbname="usersdb",
        user="admin",
        password="adminpass"
    )
    cur = conn.cursor()
    cur.execute("SELECT nombre FROM usuarios")
    rows = cur.fetchall()
    nombres = [row[0] for row in rows]
    cur.close()
    conn.close()
    return render_template_string(TEMPLATE, nombres=nombres)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
