import re

# Производится начальная сегментация текста на слова.
def get_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
        return None

# Все пунктуационные знаки удаляются, а переводы стоки заменяется на пробелы.
# Затем происходит разбитие текста на слова. В качестве разделителя по умолчанию применяется пробел.
    text = re.sub(r'[^\w\s]', '', text).replace('\n', ' ')
    words = text.lower().split()
    return words

# Получаем словарь из слов, где ключ - это уникальное слово,
# а значение - количество вхождений данного слова в тексте.
def get_words_dict(words):
    if words is None:
        return None

    words_dict = {}
    for word in words:
        words_dict[word] = words_dict.get(word, 0) + 1
    return words_dict


def print_word_stats(words_dict):
    if words_dict is None:
        return

    print(f"Кол-во слов: {len(words)}")
    print(f"Кол-во уникальных слов: {len(words_dict)}")
    print("\nВсе использованные слова:")

    for word, count in sorted(words_dict.items()):
        print(f"{word:<15} {count}")


if __name__ == "__main__":
    filename = input("Введите название файла: ")
    words = get_words(filename)
    words_dict = get_words_dict(words)
    print_word_stats(words_dict)

