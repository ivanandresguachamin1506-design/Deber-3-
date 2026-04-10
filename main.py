import qrcode
import os

def generar_qr(data, nombre_archivo):
    try:

        if not nombre_archivo.endswith(".png"):
            nombre_archivo += ".png"

        img = qrcode.make(data)
        img.save(nombre_archivo)

        ruta = os.path.abspath(nombre_archivo)
        print(f"QR guardado en: {ruta}")

    except Exception as e:
        print("Error al generar el QR:", e)

def menu():
    while True:
        print("\n=== GENERADOR DE CÓDIGOS QR ===")
        print("1. Crear QR de texto")
        print("2. Crear QR de enlace web")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            texto = input("Ingresa el texto: ")

            if texto == "":
                print("No puedes dejar el texto vacío")
                continue

            nombre = input("Nombre del archivo: ")
            generar_qr(texto, nombre)

        elif opcion == "2":
            enlace = input("Ingresa la página web (ej: google.com o https://google.com): ")

            if enlace == "":
                print("No puedes dejar el enlace vacío")
                continue

            if not enlace.startswith("http"):
                enlace = "https://" + enlace

            print(f"QR creado para la página: {enlace}")

            nombre = input("Nombre del archivo: ")
            generar_qr(enlace, nombre)

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")
menu()