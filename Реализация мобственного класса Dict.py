# 1. __init__(): Инициализация пустого словаря.
class MyDict:
    def __init__(self):
        self._data = {}

# 2. __getitem__(key): Получение значения по ключу. Если ключ не существует, вернуть None.
    def __getitem__(self, key):
        return self._data.get(key, None)

# 3. __setitem__(key, value): Установка значения по ключу.
    def __setitem__(self, key, value):
        self._data[key] = value

# 4. __delitem__(key): Удаление элемента по ключу. Если ключ не существует, ничего не делать.
    def __delitem__(self, key):
        if key in self._data:
            del self._data[key]

# 5. keys(): Возвращение списка всех ключей в словаре.
    def keys(self):
        return list(self._data.keys())

# 6. values(): Возвращение списка всех значений в словаре.
    def values(self):
        return list(self._data.values())

# 7. items(): Возвращение списка пар (ключ, значение) в словаре.
    def items(self):
        return list(self._data.items())

# 8. __str__(): Возврат строкового представления словаря для удобства отладки.
    def __str__(self):
        return str(self._data)

# Проверка наличия ключа в словаре.
    def __contains__(self, key):
        return key in self._data

# Пример использования
my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']

