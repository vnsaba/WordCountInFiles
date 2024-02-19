
# En word_counter.py
from .controller.files_controller import File
from .controller.folders_controller import Folder

class Word:
    def __init__(self, word, folder_path) -> None:
        self.word = word
        self.folder_path = folder_path

    def search_word (self):
        folder = Folder(self.folder_path)
        total = 0
        if folder.validate_folder():
            if  len(folder.get_files()) > 0:
                for f in folder.get_files() :
                    file = File(f)
                    count_word =  file.count_word(self.word)
                    total += count_word
                    print(f"{f}: {count_word} veces")
                print(f"\nTotal: {total} veces")
            else: 
                print("no text files were found in the folders")
        else:
            print("the specified folder was not found", self.folder_path)  



            



            

    


