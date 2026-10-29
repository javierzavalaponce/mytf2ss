# mytf2ss - Requisitos:

* Debian, Ubuntu, Linux Mint u otra distribución basada en Debian.
* Python 3.
* Internet durante la instalación.

## Descomprimir el proyecto

unzip mytf2ss.zip
cd mytf2ss

## Crear el entorno virtual


Un entorno virtual de Python no es mas que una carpeta
aislada que reproduce, lo más fielmente posible, 
el "python" utilizado durante el desarrollo (dev).
El entorno virtual permite instalar las bibliotecas y sus versiones sin 
afectar la instalación global de Python del sistema anfitrión (host).

python3 -m venv .venv

Este comando crea la carpeta .venv, que contendrá el entorno virtual. 
(se puede eliminar despues sin haber afectado la instalacion de Python)

Para reconstruir el entorno de desarrollo: 
las dependencias estan en requirements.txt.
ver paso sig.


## Activar el entorno virtual

source .venv/bin/activate

Aparecerá (.venv) al inicio de la línea de la terminal. Esto indica que el entorno está activo.

## Instalar las bibliotecas

python -m pip install -r requirements.txt

(toma unos dos minutos max.)

## Ejecutar el programa de prueba

python prueba_textual.py

(esta version me late mas)

## Ejecutar la aplicación web (si se desea)

python app.py

Si Flask indica que el servidor está escuchando en una dirección local, 
abrir esa dirección en el navegador: http://127.0.0.1:5000.

# Nota

Para volver a trabajar con el proyecto en otra sesión de terminal, entrar en la carpeta y activar nuevamente el entorno virtual:

cd mytf2ss
source .venv/bin/activate

Para salir del entorno virtual:

deactivate


todo esto tambien esta en install.sh
Saludos!

