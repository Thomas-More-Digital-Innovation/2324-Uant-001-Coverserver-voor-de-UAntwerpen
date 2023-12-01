# file om google drive op te kuisen naar alleen png bestanden
import pydrive

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authenticate and create the PyDrive client
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Get the list of all files in your Google Drive
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
print(file_list)
# # Define the file extension you want to keep (in this case, PNG)
# allowed_extensions = ['png']
#
# # Iterate through each file and delete non-PNG files
# for file in file_list:
#     file_extension = file['title'].split('.')[-1].lower()
#     if file_extension not in allowed_extensions:
#         print(f"Deleting file: {file['title']}")
#         file.Delete()
#
# print("Done deleting non-PNG files.")
