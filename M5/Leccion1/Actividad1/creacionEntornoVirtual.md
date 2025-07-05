### 🪟 Windows

```bash
# Crear entorno virtual llamado "venv"
python -m venv venv

# Activar entorno virtual (PowerShell)
.\venv\Scripts\Activate.ps1

# Activar entorno virtual (CMD)
.\venv\Scripts\activate.bat
```

> 💡 Si ves un error de ejecución en PowerShell, ejecuta esto una vez como administrador:

```powershell
Set-ExecutionPolicy RemoteSigned
```

---

### 🍎 macOS

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate
```

---

### 🐧 Linux

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate
```

---

### ✅ Verifica que esté activado

Una vez activado, tu terminal debería mostrar algo así:

```
(venv) user@machine:~$
```

Y puedes verificarlo con:

```bash
which python   # macOS/Linux
where python   # Windows
```
