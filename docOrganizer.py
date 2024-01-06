import os
from tkinter.filedialog import askdirectory

folder_path = askdirectory(title="Select a folder")

file_list = os.listdir(folder_path)

locations = {
    "images": [".png", ".jpg"],
    "spreadsheets": [".xlsx"],
    "pdfs": [".pdf"],
    "csv":[".csv"]
}

for file in file_list:
    name, extension = os.path.splitext(f"{folder_path}/{file}")
    for folder in locations:
        if extension in locations[folder]:
            if not os.path.exists(f"{folder_path}/{folder}"):
                os.mkdir(f"{folder_path}/{folder}")
            os.rename(f"{folder_path}/{file}", f"{folder_path}/{folder}/{file}")