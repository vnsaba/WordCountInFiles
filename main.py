from src.word_counter import Word

folder_path = input("Enter the folder path: ")
word_input = input("Enter the word to search for: ")
word = Word(word_input, folder_path)
word.search_word()
