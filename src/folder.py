#manejar los carchivos
import os 
from file import File
class Folder:
    def __init__(self, folder_path, word) -> None:
        self.folder_path = folder_path
        self.word = word
        self.listFiles = []
        
    def validate_folder (self):
        return  os.path.isdir(self.folder_path) and os.path.exists(self.folder_path)
    
    def get_files (self):
        for f in os.listdir(self.folder_path):
                file_path = os.path.join(self.folder_path, f)
                file  = File(file_path)
                if  file.validate_file():
                    self.listFiles.append(file_path)
        return self.listFiles
    
    def search_word (self):
        total = 0
        if self.validate_folder():
            if  len(self.get_files()) > 0:
                for f in self.listFiles:
                    file = File(f)
                    count_word =  file.count_word(self.word)
                    total += count_word
                    print(f"{f}: {count_word} veces")
                print(f"\nTotal: {total} veces")
            else: 
                print("no text files were found in the folders")
        else:
            print("the specified folder was not found", self.folder_path)  

    
