from folder import Folder

folder_path = input("Enter the folder path: ")
word_input = input("Enter the word to search for: ")
word = Folder(folder_path, word_input)
word.search_word()
