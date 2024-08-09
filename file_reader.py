def read_words(file_path):
    """Читает слова из файла и возвращает их в виде списка."""
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().splitlines()
    return words