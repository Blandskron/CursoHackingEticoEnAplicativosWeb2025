# Generador de Informes Blandskron (PDF/Word)

App web mínima (Flask) para crear informes estandarizados con tu branding y exportar a **PDF (WeasyPrint)** o **Word (.docx)**.

## Requisitos
- Python 3.10+
- Linux/Mac/WSL recomendado (WeasyPrint necesita libffi, libpango, etc.)

## Instalación
```bash
cd reportgen
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
pip install -r requirements.txt
```

> **WeasyPrint** requiere dependencias del sistema (Debian/Ubuntu):
```bash
sudo apt-get install -y libpango-1.0-0 libpangoft2-1.0-0 libcairo2 libffi8
```

## Uso
```bash
python app.py
# abre http://localhost:5000
```
1) Completa los inputs en la portada y secciones.  
2) Previsualiza el diseño.  
3) Exporta en **PDF** o **Word** con un clic.

## Logo
Los logos están en `static/img/logo-horizontal.png` y `static/img/logo-icon.png`. Reemplázalos por tus archivos si los cambias.

## Tabla de hallazgos
Opcionalmente pega líneas en el área de texto con el formato:
```
Hallazgo | Impacto | Criticidad | Recomendación
```
Una línea por hallazgo.

---
Made with ❤️ para Blandskron.
