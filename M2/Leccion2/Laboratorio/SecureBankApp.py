# Simulación del sitio analizado para SecureBank S.A.
# Vulnerabilidades intencionadas: SQLi, Admin sin protección, XSS persistente

from flask import Flask, request, session, redirect, render_template_string
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Ruta de la base de datos
DB_PATH = 'securebank.db'
# Almacenamiento de mensajes de contacto (XSS)
CONTACTS = []

# Inicialización de base de datos SQLite
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        );
    ''')
    # Usuario por defecto
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'admin123');")
    conn.commit()
    conn.close()

# Vulnerable a SQL Injection: concatenación de inputs sin sanitizar
def query_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    sql = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';"
    # La consulta se ejecuta tal cual y explotable vía SQLi
    user = c.execute(sql).fetchone()
    conn.close()
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form.get('username', '')
        pwd = request.form.get('password', '')
        user = query_user(uname, pwd)
        if user:
            session['user'] = user[1]
            return redirect('/dashboard')
        return 'Credenciales inválidas', 401
    # Formulario simple
    return render_template_string('''
        <h2>Login</h2>
        <form method="post">
            Usuario: <input name="username"><br>
            Contraseña: <input name="password" type="password"><br>
            <button type="submit">Ingresar</button>
        </form>
    ''')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    return f"<h1>Bienvenido, {session['user']}!</h1>"

@app.route('/admin')
def admin_panel():
    # Panel administrativo sin protección
    return '<h1>Panel Admin</h1><p>Acceso sin autenticación</p>'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '')
        message = request.form.get('message', '')
        # XSS persistente: almacena entradas sin escapar
        CONTACTS.append({'name': name, 'message': message})
        return redirect('/contact')
    # Renderiza mensajes sin sanitizar
    entries = ''.join([f"<div><strong>{e['name']}</strong>: {e['message']}</div>" for e in CONTACTS])
    return render_template_string(f'''
        <h2>Contacto</h2>
        {entries}
        <form method="post">
            Nombre: <input name="name"><br>
            Mensaje: <textarea name="message"></textarea><br>
            <button type="submit">Enviar</button>
        </form>
    ''')

if __name__ == '__main__':
    init_db()
    print("Servidor arrancando en http://127.0.0.1:5000")
    app.run(debug=True)
