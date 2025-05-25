# Задача 1: Комбинации чисел из списка
# Дан список чисел [1, 2, 3, 4]. Используя модуль itertools, создайте все возможные комбинации чисел длиной 2
# и выведите их.


import itertools

items = [1, 2, 3, 4]
for c in itertools.combinations(items, 2):
    print(c)


# Задача 2: Перебор перестановок букв в слове
# Для слова 'Python' найдите все возможные перестановки букв. Выведите каждую перестановку на отдельной строке.


import itertools

items = ['p', 'y', 't', 'h', 'o', 'n']
for p in itertools.permutations(items):
    print(p)


# Задача 3: Объединение списков в цикле
# Даны три списка: ['a', 'b'], [1, 2, 3], ['x', 'y']. Используя itertools.cycle, объедините их в один список в
# цикле, повторяя этот цикл 5 раз.

import itertools

list1 = ['a', 'b']
list2 = [1, 2, 3]
list3 = ['x', 'y']

combined_list = list1 + list2 + list3
cycler = itertools.cycle(combined_list)
result = []
total_iterations = len(combined_list) * 5

for _ in range(total_iterations):
    result.append(next(cycler))

print(result)

# Задача 4: Генерация бесконечной последовательности чисел
# Создайте бесконечный генератор, который будет возвращать последовательность чисел Фибоначчи. Выведите первые
# 10 чисел Фибоначчи.


import itertools

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()

first10 = list(itertools.islice(fib_gen, 10))

print(first10)


# Задача 5: Составление всех возможных комбинаций слов
# Используя itertools.product, создайте все возможные комбинации слов из двух списков: ['red', 'blue'] и
# ['shirt', 'shoes']. Выведите каждую комбинацию на отдельной строке.

import itertools


colors = ['red', 'blue']
items = ['shirt', 'shoes']

combinations = itertools.product(colors, items)

for i in combinations:
    print(' '.join(i))