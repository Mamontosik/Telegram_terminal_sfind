def read_words(file_path):
    """Читает слова из файла и возвращает их в виде списка."""
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().splitlines()
    return words

def compare_words(words):
    """Сравнивает слова между собой и выводит результаты сравнения."""
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1 = words[i]
            word2 = words[j]
            if word1 == word2:
                print(f"Слова '{word1}' и '{word2}' одинаковы.")
            else:
                print(f"Слова '{word1}' и '{word2}' различны.")
            common_chars = compare_characters(word1, word2)
            if common_chars:
                print(f"Слова '{word1}' и '{word2}' имеют одинаковые символы на тех же местах: {common_chars}")

def compare_characters(word1, word2):
    """Сравнивает символы двух слов и возвращает список одинаковых символов на тех же местах."""
    common_chars = []
    min_length = min(len(word1), len(word2))
    for k in range(min_length):
        if word1[k] == word2[k]:
            common_chars.append((k, word1[k]))
    return common_chars

def main():
    file_path = 'words.txt'
    words = read_words(file_path)
    compare_words(words)

if __name__ == "__main__":
    main()