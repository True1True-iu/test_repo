# 1. __init__(): Инициализация пустого словаря.
class MyDict:
    def __init__(self):
        self._items = []

# 2. __getitem__(key): Получение значения по ключу. Если ключ не существует, вернуть None.
    def __getitem__(self, key):
        for k, v in self._items:
            if k == key:
                return v
        return None

# 3. __setitem__(key, value): Установка значения по ключу.
    def __setitem__(self, key, value):
        for i, (k, v) in enumerate(self._items):
            if k == key:
                self._items[i] = (key, value)
                return
        self._items.append((key, value))  

# 4. __delitem__(key): Удаление элемента по ключу. Если ключ не существует, ничего не делать.
    def __delitem__(self, key):
        for i, (k, v) in enumerate(self._items):
            if k == key:
                del self._items[i]
                return

# 5. keys(): Возвращение списка всех ключей в словаре.
    def keys(self):
        return [k for k, v in self._items]

# 6. values(): Возвращение списка всех значений в словаре.
    def values(self):
        return [v for k, v in self._items]

# 7. items(): Возвращение списка пар (ключ, значение) в словаре.
    def items(self):
        return self._items

# 8. __str__(): Возврат строкового представления словаря для удобства отладки.
    def __str__(self):
        return "{" + ", ".join(f"{k}: {v}" for k, v in self._items) + "}"

# Проверка наличия ключа в словаре.
    def __contains__(self, key):
        return any(k == key for k, v in self._items)

my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']

