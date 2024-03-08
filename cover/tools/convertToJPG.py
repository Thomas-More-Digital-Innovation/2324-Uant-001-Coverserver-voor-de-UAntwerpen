# adhv dit script convert je alle images naar JPG en spoor je corrupted files op
from PIL import Image
import os

def convert_to_jpg(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if the file is an image
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpeg', '.jpg', '.gif')):
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")

            # Open the image and save it as JPG
            try:
                img = Image.open(input_path)
                img.convert("RGB").save(output_path, "JPEG")
            except Exception as e:
                print(f"Error converting {filename}: {str(e)}")

if __name__ == "__main__":
    input_folder_good = r"C:\covers\goede_covers"
    output_folder_good = r"C:\covers\converted\goede_covers"

    input_folder_bad = r"C:\covers\slechte_covers"
    output_folder_bad = r"C:\covers\converted\slechte_covers"

    convert_to_jpg(input_folder_good, output_folder_good)
    convert_to_jpg(input_folder_bad, output_folder_bad)
