import os
import shutil

def move_files(start_dir, end_dir):
    if not os.path.exists(end_dir):
        print("no existe wacho")
        return

    files = os.listdir(start_dir)

    for file in files:
        start_dir = os.path.join(start_dir, file)
        destination_path = os.path.join(end_dir, file)
        
        if os.path.isfile(start_dir):
            shutil.move(start_dir, destination_path)
            print(f"esto ('{file}') te lo puse aca ('{end_dir}')")
        else:
            print(f"'{file}' no es un archivo te lo dejo aca <3")


start_dir = "path del primer dir"
end_dir = "path del ultimo dir"

move_files(start_dir, end_dir)
