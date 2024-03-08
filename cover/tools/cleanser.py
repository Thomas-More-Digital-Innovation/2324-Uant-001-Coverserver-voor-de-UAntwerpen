# script to delete non jpg files from my drive
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Get the path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))
client_secrets_path = os.path.join(script_dir, 'client_secrets.json')

# Authenticate and create the PyDrive client
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

# Get the ID of the specific folder you want to clean up
folder_name = 'slechte_covers'
folder_query = f"title = '{folder_name}' and trashed=false"
folder_list = drive.ListFile({'q': folder_query}).GetList()

if not folder_list:
    print(f"Folder '{folder_name}' not found.")
    exit()

# Get the ID of the folder
folder_id = folder_list[0]['id']

file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()

allowed_extensions = ['jpg']

for file in file_list:
    file_extension = file['title'].split('.')[-1].lower()
    if file_extension not in allowed_extensions:
        print(f"Deleting file: {file['title']}")
        file.Delete()

print("Done deleting non-JPG files.")
