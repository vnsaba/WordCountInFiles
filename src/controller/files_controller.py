
import os 
import re

class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def validate_file (self):
        extension = ['.txt', '.csv', '.xlm', '.json']
        _, file_extension = os.path.splitext(self.file_path)
        return os.path.isfile(self.file_path) and file_extension in extension 
    
    def count_word(self, word):
        if self.validate_file():
            with open(self.file_path, 'r', encoding='utf-8') as file:
                content_file = file.read().lower()
                incidents_word = re.findall(r'\b' + re.escape(word.lower()) + r'\b', content_file)
            return len(incidents_word)
        return 0
