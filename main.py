# Самостоятельная работа по уроку "Произвольное число параметров"

def single_root_words(root_word, *other_words):
    # Приводим корневое слово к нижнему регистру
    root_word_lower = root_word.lower()
    same_words = []  # Список для хранения однокоренных слов

    # Перебираем все слова из other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()

        # Проверяем, содержится ли корневое слово в текущем слове или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)  # Добавляем слово в список, если условие выполнено

    return same_words  # Возвращаем список однокоренных слов

# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Выводим результаты
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']
