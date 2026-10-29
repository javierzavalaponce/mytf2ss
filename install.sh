#!/bin/bash

set -e

echo "=== Instalando mytf2ss ==="

# Verificar Python
python3 --version

# Crear entorno virtual
echo "Creando entorno virtual..."
python3 -m venv .venv

# Activar entorno virtual
source .venv/bin/activate

# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias
echo "Instalando dependencias..."
python -m pip install -r requirements.txt

echo ""
echo "=== Instalación terminada ==="
echo "Para ejecutar el programa:"
echo "  source .venv/bin/activate"
echo "  python prueba_textual.py"


