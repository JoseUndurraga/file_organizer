import os
from pathlib import Path
import shutil
import argparse

cwd = os.getcwd()

default_folder = "Organize"

names = ["Datasets","Docs","Images","Not Considered"]

Datasets = [".csv",".tsv",".txt",".xlsx",".xls",".ods",".json",".xml",".yaml",".yml",".parquet",".feather",".h5",".hdf5",".pkl",".pickle",".sql",".sqlite",".db"]

Docs = [".pdf",".djvu",".docx",".doc",".odt",".rtf",".pptx",".ppt",".odp",".md",".tex",".rst",".epub"]

Images= [".jpg",".jpeg",".png",".webp",".heic",".svg",".ai",".eps",".gif",".tiff",".tif",".bmp",".raw",".cr2",".nef"]

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Files Organizer")

    parser.add_argument("path_of_organize_folder", nargs = "?", default = default_folder)

    arguments = parser.parse_args()

    organize_path = Path(arguments.path_of_organize_folder)

    organize_path = organize_path.resolve()

    if not organize_path.exists():
        
        raise FileNotFoundError("Directorio no encontrado")

    organize_generator = organize_path.iterdir()

    directory_lists = []

    for path in names:

        directory = cwd + "\\" + path
        directory = Path(directory)

        directory_lists.append(directory)

        if not directory.exists():

            os.mkdir(directory)

    for path in organize_generator:

        if path.is_file():

            (name, extension) = os.path.splitext(path)
            extension = extension.lower()

            if extension in Datasets:
                shutil.move(path, directory_lists[0])
            elif extension in Docs:
                shutil.move(path, directory_lists[1])
            elif extension in Images:
                shutil.move(path, directory_lists[2])
            else:
                shutil.move(path, directory_lists[3])
            


            


    
            

    

