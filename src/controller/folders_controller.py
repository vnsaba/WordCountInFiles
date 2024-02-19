#manejar los carchivos
import os 
from .files_controller import File
class Folder:
    def __init__(self, folder_path) -> None:
        self.folder_path = folder_path
        
    def validate_folder (self):
        return  os.path.isdir(self.folder_path) and os.path.exists(self.folder_path)
    
    #listar todos los archivos de textos que hay en el directorio
    def get_files (self):
        listFiles = []  # Reiniciar la lista para cada llamada
        for f in os.listdir(self.folder_path):
                #unir toda la direccion
                file_path = os.path.join(self.folder_path, f)
                #verificar que sea un archivo y que sea de tipo texto
                file  = File(file_path)
                if  file.validate_file():
                    listFiles.append(file_path)
        return listFiles
    
