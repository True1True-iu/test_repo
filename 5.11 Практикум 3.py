# 1. Сгенерируйте список всех карт в стандартной колоде.
# 2. Генерация комбинаций: Используйте модуль itertools, чтобы получить все комбинации из заданного числа карт.
# 3. Вывод результатов: Выведите все комбинации на экран или сохраните их в файл для последующего использования.

import itertools

# 1. Генерируем список всех карт в стандартной колоде.
def create_deck():
    suits = ['Пики', 'Черви', 'Бубны', 'Трефы']
    ranks = [' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', ' 10 ', ' Валет ', ' Дама ', ' Король ', ' Туз ']
    deck = [rank + suit for suit in suits for rank in ranks]
    return deck

# 2. Генерация комбинаций
def generate_combinations(deck, num_cards):
    return itertools.combinations(deck, num_cards)

deck = create_deck()

# 3. Вывод результатов
print(deck)

