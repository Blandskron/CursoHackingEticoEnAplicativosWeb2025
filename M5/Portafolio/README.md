# Portafolio Módulo 5 - Hacking Ético en Aplicaciones Web

Este proyecto incluye un conjunto de herramientas de análisis y pruebas de seguridad en entornos controlados. Cada script ejecuta una función específica: reconocimiento de objetivos, escaneo de puertos, detección de vulnerabilidades SQLi y XSS, y generación automática de reportes.

## Requisitos Previos

Antes de ejecutar los scripts, asegúrate de instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Instrucciones de Ejecución

### 1. Reconocimiento de subdominios y cabeceras

**Archivo:** `reconocimiento.py`

```bash
python reconocimiento.py -d ejemplo.com
```

Realiza reconocimiento pasivo incluyendo subdominios, tecnologías y cabeceras HTTP. El resultado se guarda automáticamente en un archivo JSON.

### 2. Escaneo de Puertos

**Archivo:** `scanner.py`

```bash
python scanner.py -t 127.0.0.1 --start-port 1 --end-port 1024
```

Escanea los puertos TCP del objetivo especificado. Los resultados se muestran por consola.

### 3. Detección de SQL Injection

**Archivo:** `sqli_tester.py`

```bash
python sqli_tester.py -u "https://ejemplo.com/item?id="
```

Realiza pruebas automatizadas de SQL Injection (error-based y lógica booleana). Los resultados se guardan en `sqli_results.json`.

### 4. Detección de XSS Reflejado

**Archivo:** `xss_checker.py`

```bash
python xss_checker.py -u "https://ejemplo.com/search?q="
```

Ejecuta payloads comunes de Cross-Site Scripting (XSS) y detecta si alguno es reflejado en la respuesta. El resultado se guarda en `xss_results.json`.

### 5. Generación de Reporte Final en Word

**Archivo:** `report_generator.py`

```bash
python report_generator.py
```

Genera un archivo `.docx` con los resultados obtenidos de los análisis SQLi y XSS. El documento final se llama `informe_final.docx`.

## Estructura del Proyecto

```
├── reconocimiento.py
├── scanner.py
├── sqli_tester.py
├── xss_checker.py
├── report_generator.py
├── requirements.txt
├── sqli_results.json
├── xss_results.json
└── informe_final.docx
```
