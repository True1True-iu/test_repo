# Описание

Данный скрипт реализует класс `Student`, который представляет студента с основными характеристиками:
имя, возраст, специальность и средний балл (GPA).
Он также предоставляет методы для отображения информации о студенте и вычисления оценки на основе его
среднего балла.

## Класс Student

### Поля

- `name` (str): Имя студента
- `age` (int): Возраст студента
- `major` (str): Специальность студента
- `gpa` (float): Средний балл студента (GPA)

### Методы

- `display_info()`: Выводит информацию о студенте в удобном для чтения формате.
  
''' python
def display_info(self):
print(f"Имя: {self.name}")
print(f"Возраст: {self.age}")
print(f"Специальность: {self.major}")
print(f"Средний балл студента: {self.gpa}")
'''

- `calculate_grade()`: Определяет оценку студента на основе его GPA.
  

  def calculate_grade(self):
      if self.gpa >= 4.0:
          return "Отлично"
      elif self.gpa >= 3.0:
          return "Хорошо"
      elif self.gpa >= 2.0:
          return "Удовлетворительно"
      else:
          return "Неудовлетворительно"

## Установка

Для запуска данного скрипта требуется Python 3.6 и выше. Вы можете просто скопировать и вставить код
в файл `.py` и выполнить его с помощью Python
