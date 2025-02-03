def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return "File not found. Please check the file path."

# Example usage
file_path = 'path/to/your/file.txt'
word_count = count_words(file_path)
print(f'The number of words in the file is: {word_count}')
