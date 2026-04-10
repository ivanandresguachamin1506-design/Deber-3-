# Generador de Códigos QR

## Estudiante
Ivan Andres Guachamin Guevara

## Librería utilizada
qrcode

##  Descripción
Este programa permite generar códigos QR a partir de texto o enlaces web ingresados por el usuario. Además, corrige automáticamente los enlaces agregando el prefijo "https://" si el usuario no lo incluye.

##  Instalación

Primero, instalar la librería necesaria:

pip install qrcode[pil]

##  Ejecución

Ejecutar el programa con:

python main.py

##  Funcionalidades

- Generar QR de texto
- Generar QR de enlaces web
- Corrección automática de enlaces
- Guardado automático en formato PNG
- Validación básica de entradas

##  Ejemplo de uso

1. Ejecutar el programa
2. Elegir opción 2
3. Ingresar: google.com
4. Guardar como: qr1

Resultado: Se genera un archivo qr1.png que al escanear abre Google.
