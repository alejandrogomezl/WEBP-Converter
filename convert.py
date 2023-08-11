from PIL import Image
import os

def convert_to_webp(input_path, output_path):
    try:
        img = Image.open(input_path)
        if img.mode != "RGB":
            img = img.convert("RGB")
        
        output_filename = os.path.splitext(os.path.basename(input_path))[0] + ".webp"
        output_file = os.path.join(output_path, output_filename)
        
        img.save(output_file, "WEBP")
        print(f"Archivo convertido y guardado como {output_file}")
    except Exception as e:
        print(f"Error al convertir el archivo {input_path}: {e}")

def delete_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Archivo eliminado: {file_path}")
        except Exception as e:
            print(f"Error al eliminar el archivo {file_path}: {e}")        

input_folder = "carpeta_input"
output_folder = "carpeta_output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.png')):
        input_file = os.path.join(input_folder, filename)
        convert_to_webp(input_file, output_folder)

delete_files_in_folder(input_folder)