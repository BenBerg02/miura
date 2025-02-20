import argparse
import os
from PIL import Image

def images_to_pdf(input_folder, output_pdf):
    # Obtener todas las imágenes de la carpeta ordenadas alfabéticamente
    image_paths = sorted(
        [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    )

    if not image_paths:
        print("No se encontraron imágenes en la carpeta proporcionada.")
        return

    # Abrir la primera imagen
    first_image = Image.open(image_paths[0]).convert("RGB")
    
    # Abrir las demás imágenes y convertirlas a RGB
    images = [Image.open(img).convert("RGB") for img in image_paths[1:]]
    
    # Guardar en un PDF
    first_image.save(output_pdf, save_all=True, append_images=images)
    print(f"PDF generado: {output_pdf}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convierte imágenes de una carpeta en un PDF.")
    parser.add_argument("input_folder", help="Carpeta que contiene las imágenes")
    parser.add_argument("output_pdf", help="Nombre del archivo PDF de salida")

    args = parser.parse_args()
    images_to_pdf(args.input_folder, args.output_pdf)
