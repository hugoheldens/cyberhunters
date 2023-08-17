import requests
import os
import io
from PIL import Image, ImageOps  # Importar ImageOps desde PIL
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def descargar_libro(url_libro, paginas, nombre_libro):
    imagenes = []  # Arreglo para almacenar las imágenes
    cont = 1
    while paginas > cont:
        numero_con_ceros_a_la_izquierda = f"{cont:03d}"
        url_imagen = f"{url_libro[:-4]}/{cont:03d}.jpg"
        print(url_imagen)
        nombre_local_imagen = f"{nombre_libro}_{cont:03d}.jpg"

        # URL de la imagen que deseas descargar
        image_url = url_imagen

        # Realizar la solicitud HTTP para obtener la imagen
        img_response = requests.get(image_url)

        # Verificar que la solicitud se haya realizado correctamente
        if img_response.status_code == 200:
            imagen = Image.open(io.BytesIO(img_response.content))
            imagenes.append(imagen)
            cont += 1
            print(cont)
            print(f'Imagen {nombre_local_imagen} descargada.')
        else:
            print(f'No se pudo descargar la imagen {nombre_local_imagen}.')
            cont -= 1
            print(cont)
            break

    # Crear la carpeta para las imágenes
    carpeta_imagenes = nombre_libro
    os.makedirs(carpeta_imagenes, exist_ok=True)

    # Guardar las imágenes en la carpeta
    for i, imagen in enumerate(imagenes, start=1):
        imagen.save(os.path.join(carpeta_imagenes, f"imagen_{i:03d}.jpg"))

    # Crear el PDF con las imágenes
    pdf_filename = f"{nombre_libro}.pdf"
    pdf = canvas.Canvas(pdf_filename, pagesize=letter)


    for i in range(1, cont + 1):
        image_path = os.path.join(carpeta_imagenes, f"imagen_{i:03d}.jpg")

        try:
            pdf.drawImage(image_path, 0, 0, width=letter[0], height=letter[1])
            pdf.showPage()
        except FileNotFoundError:
            print(f'La imagen {image_path} no se encontró. Generando PDF con imágenes hasta la página {i - 1}.')
            break

    pdf.save()
    print(f'Se ha creado el PDF {pdf_filename} con las imágenes.')

    # Eliminar la carpeta de imágenes
    for i in range(1, cont + 1):
        image_path = os.path.join(carpeta_imagenes, f"imagen_{i:03d}.jpg")
        if os.path.exists(image_path):
            os.remove(image_path)
    os.rmdir(carpeta_imagenes)
# Pide al usuario que ingrese un número del 1 al 6
Grado_Primaria = int(input("Elige el grado de primaria: "))

# Verifica si el número ingresado es válido
if Grado_Primaria < 1 or Grado_Primaria > 6:
    print("Número inválido. Debe ser del 1 al 6.")
else:
    # Pregunta al usuario qué libro quiere
    print("¿Qué libro quieres?")
    print("1. Un libro sin recetas")
    print("2. Multiples lenguajes")
    print("3. Libro de proyectos de Aula")
    print("4. Libro de proyectos Comunitarios")
    print("5. Libro de proyectos Escolares")
    print("6. Nuestros Saberes")
    print("7. Multiples lenguajes, Trazos y palabras")

    opcion_libro = int(input("Selecciona una opción del 1 al 7: "))

    # Asigna el valor correspondiente a la variable "Libro" según la opción elegida
    if opcion_libro == 1:
        Libro = "LPM"
    elif opcion_libro == 2:
        Libro = "MLA"
    elif opcion_libro == 3:
        Libro = "PAA"
    elif opcion_libro == 4:
        Libro = "PCA"
    elif opcion_libro == 5:
        Libro = "PEA"
    elif opcion_libro == 6:
        Libro = "SDA"
    elif opcion_libro == 7:
        Libro = "TPA"
    else:
        print("Opción inválida. Debe ser del 1 al 7.")

elemento = f'P{Grado_Primaria}{Libro}'
url_libro = f'https://www.conaliteg.sep.gob.mx/2023/c/{elemento}.htm'
descargar_libro(url_libro, 500, elemento)