# Escáner Avanzado de Subred con Nmap en Python

Este proyecto permite escanear subredes completas utilizando **Nmap** mediante un script en Python. Detecta hosts activos, analiza puertos abiertos, servicios, versiones y guarda los resultados en un archivo JSON estructurado.


## Requisitos

- Python 3.8+
- Nmap instalado y accesible en la terminal
- Bibliotecas de Python:
  - `python-nmap`
  - `tqdm`


## Instalación

### Windows

1. **Instalar Nmap**:
   - Descargar desde: https://nmap.org/download.html (versión con instalador)
   - Asegúrate de marcar la opción “Add Nmap to PATH”.

2. **Instalar dependencias de Python**:
   ```powershell
   pip install python-nmap tqdm
   ```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install nmap python3-pip
pip3 install python-nmap tqdm
```

### macOS

```bash
brew install nmap
pip3 install python-nmap tqdm
```


## Uso

```bash
python escaneo_subred.py -s <subred> -a <argumentos_nmap> -o <archivo_salida>
```

* `-s`, `--subred`: Subred objetivo en formato CIDR (ej: `192.168.1.0/24`)
* `-a`, `--argumentos`: Argumentos adicionales para Nmap (como `-sS -sV -O -T4`)
* `-o`, `--output`: Nombre del archivo JSON donde guardar resultados (por defecto: `resultados_escaneo.json`)

## Ejemplos de uso

### Escaneo rápido con detección de puertos comunes

```bash
python escaneo_subred.py -s 192.168.1.0/24 -a -T4 -F
```

### Escaneo SYN + versiones + sistema operativo

```bash
python escaneo_subred.py -s 192.168.1.0/24 -a -sS -sV -O -T3
```

### Escaneo completo de todos los puertos (puede tardar)

```bash
python escaneo_subred.py -s 192.168.1.0/24 -a -p- -sS -sV -O -T3
```

## Resultado

Los resultados se guardan en un archivo JSON estructurado como este:

```json
[
  {
    "host": "192.168.1.12",
    "estado": "up",
    "puertos": [
      { "puerto": 80, "estado": "open", "servicio": "http", "version": "" }
    ]
  }
]
```

## Consejos

* Usa `-T4` o `-T5` para escaneos más rápidos (aunque menos sigilosos).
* Usa `-sS` para escaneo SYN, `-sV` para detección de versión, `-O` para sistema operativo.
* Evita saturar la red si hay muchos hosts.

## Uso Responsable

Este script debe utilizarse **solo en redes que administras o tienes permiso de auditar.** No lo uses en redes externas sin autorización previa. El uso indebido de Nmap puede considerarse una actividad maliciosa.

```bash
# Escaneo rápido
python escaneo_subred.py -s 192.168.1.0/24 -a -T4 -F

# Escaneo de SYN + detección de versión + OS detection
python escaneo_subred.py -s 192.168.1.0/24 -a -sS -sV -O -T3

# Escaneo completo de todos los puertos con escaneo agresivo
python escaneo_subred.py -s 192.168.1.0/24 -a -p- -A -T3
```