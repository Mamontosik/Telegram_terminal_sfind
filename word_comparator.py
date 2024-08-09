def compare_words(words):
    """Сравнивает слова между собой и выводит результаты сравнения."""
    match_counts = [0] * len(words)  # Список для подсчета совпадений для каждого слова

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1 = words[i]
            word2 = words[j]
            if word1 == word2:
                print(f"Слова '{word1}' и '{word2}' одинаковы.")
            else:
                print(f"Слова '{word1}' и '{word2}' различны.")
            common_chars, common_count = compare_characters(word1, word2)
            if common_chars:
                print(f"Слова '{word1}' и '{word2}' имеют одинаковые символы на тех же местах: {common_chars}")
                print(f"Количество одинаковых символов на тех же местах: {common_count}")
                # Увеличиваем счетчик совпадений для обоих слов
                match_counts[i] += common_count
                match_counts[j] += common_count

    # Находим слово с наибольшим количеством совпадений
    max_matches = max(match_counts)
    most_matching_word = words[match_counts.index(max_matches)]
    print(f"Слово с наибольшим количеством совпадений символов: '{most_matching_word}' с {max_matches} совпадениями.")

def compare_characters(word1, word2):
    """Сравнивает символы двух слов и возвращает список одинаковых символов на тех же местах и их количество."""
    common_chars = []
    min_length = min(len(word1), len(word2))
    for k in range(min_length):
        if word1[k] == word2[k]:
            common_chars.append((k, word1[k]))
    common_count = len(common_chars)
    return common_chars, common_count