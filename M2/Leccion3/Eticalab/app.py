from flask import Flask, render_template
from flask import request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, correo, rol FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return render_template("index.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)
