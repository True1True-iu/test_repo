# 1. Используйте map(), чтобы преобразовать список чисел в список их кубов, используя обычную
# функцию.


def cube(x):
    return x ** 3

numbers = [1, 2, 3, 4, 5]
cubes = list(map(cube, numbers))
print(cubes)


# 2. Используйте filter(), чтобы отобрать из списка чисел только те, которые делятся на 5,
# используя обычную функцию.


def is_divisible_by_5(x):
    return x % 5 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(is_divisible_by_5, numbers))
print(filtered_numbers)


# 3. Используйте  filter() и  reduce(), чтобы найти произведение всех нечетных чисел в списке,
# используя обычную функцию.


from functools import reduce

def is_odd(x):
    return x % 2 != 0

def multiply(x, y):
    return x * y

def multiply_odd_numbers(numbers):
    odd_numbers = filter(is_odd, numbers)
    product = reduce(multiply, odd_numbers)
    return product

numbers = [1, 2, 3, 4, 5]
print(multiply_odd_numbers(numbers))