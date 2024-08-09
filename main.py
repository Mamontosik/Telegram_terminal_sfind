from file_reader import read_words
from word_comparator import compare_words

def main():
    file_path = 'words.txt'
    words = read_words(file_path)
    compare_words(words)

if __name__ == "__main__":
    main()