# Задание 0. Работа с json
# Считайте данные из файла student_list.json и преобразуйте в словарь students.

import json
import csv

def load_students_from_json(filename="student_list.json"):

  try:
    with open(filename, 'r', encoding='utf-8') as f:
      students = json.load(f)
    return students
  except FileNotFoundError:
    print(f"Ошибка: Файл '{filename}' не найден.")
    return None
  except json.JSONDecodeError:
    print(f"Ошибка: Не удалось декодировать JSON из файла '{filename}'.  Проверьте его формат.")
    return None
  except Exception as e:
    print(f"Произошла непредвиденная ошибка при чтении файла '{filename}': {e}")
    return None


students = load_students_from_json()

if students:
  print("Данные о студентах успешно загружены:")
  print(students)
else:
  print("Не удалось загрузить данные о студентах.")


# # Задание 1: Средний балл по всем предметам
# # Напишите функцию get_average_score(), которая вычисляет средний балл по всем предметам
# # для каждого студента в словаре students.


def get_average_score(students):

    for name, data in students.items():
        grades = data.get('grades', {})
        if grades:
            avg = sum(grades.values()) / len(grades)
        else:
            avg = 0
        print(f"Средний балл для студента {name}: {avg}")

# Вызов функции:
get_average_score(students)


# Задание 2: Наилучший и худший студент
# Напишите функции get_best_student() и get_worst_student(), которые находят студента с
# наилучшим и худшим средним баллом соответственно. Выведите их имена и средние баллы
# Наилучший студент: Sophia (Средний балл: 90.67)
# Худший студент: Robert (Средний балл: 83.67)


def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)

def get_best_student(students):
    best_name = None
    best_avg = -1
    for name, data in students.items():
        avg = calculate_average(data.get('grades', {}))
        if avg > best_avg:
            best_avg = avg
            best_name = name
    return best_name, best_avg

def get_worst_student(students):
    worst_name = None
    worst_avg = float('inf')
    for name, data in students.items():
        avg = calculate_average(data.get('grades', {}))
        if avg < worst_avg:
            worst_avg = avg
            worst_name = name
    return worst_name, worst_avg

best_name, best_avg = get_best_student(students)
worst_name, worst_avg = get_worst_student(students)

print()
print(f"Наилучший студент: {best_name} (Средний балл: {best_avg:.2f})")
print(f"Худший студент: {worst_name} (Средний балл: {worst_avg:.2f})")


# Задание 3: Поиск по имени
# Напишите функцию find_student(name), которая принимает имя студента в качестве аргумента
# и выводит информацию о нем, если такой студент есть в словаре students. В противном случае,
# выведите сообщение "Студент с таким именем не найден".


def find_student(name, students):

    if name in students:
        student = students[name]
        print(f"Имя: {name}")
        print(f"Возраст: {student['age']}")
        print(f"Предметы: {student['subjects']}")
        print(f"Оценки: {student['grades']}")
    else:
        print("Студент с таким именем не найден")

if students:
    print()
    find_student("John", students)
    print()
    find_student("Anna", students)


# Задание 4: Сортировка студентов
# Отсортируйте студентов по их среднему баллу в порядке убывания. Выведите имена студентов
# и их средние баллы в следующем формате:


def calculate_average_grade(grades):

  if not grades:
    return 0.0
  return round(sum(grades.values()) / len(grades), 2)


def sort_students_by_average(students):

  student_averages = {}
  for name, data in students.items():
    student_averages[name] = calculate_average_grade(data.get("grades", {}))

  sorted_students = sorted(student_averages.items(), key=lambda item: item[1], reverse=True)
  return sorted_students

sorted_students = sort_students_by_average(students)

print("Сортировка студентов по среднему баллу:")
for name, average_grade in sorted_students:
  print(f"{name}: {average_grade}")


# Задание 5. Преобразуйте словарь в список словарей данного формата
# students = [
#     {
#         'name': 'John',
#         'age': 20,
#         'subjects': ['Math', 'Physics', 'History', 'Chemistry', 'English'],
#         'grades': {'Math': 95, 'Physics': 88, 'History': 72, 'Chemistry': 84, 'English': 90}
#     },
#     {
#         'name': 'Alice',
#         'age': 19,
#         'subjects': ['Biology', 'Chemistry', 'Literature', 'Math', 'Art'],
#         'grades': {'Biology': 80, 'Chemistry': 92, 'Literature': 78, 'Math': 88, 'Art': 86}
#     },
#     {
#         'name': 'Michael',
#         'age': 22,
#         'subjects': ['Computer Science', 'English', 'Art', 'History', 'Economics'],
#         'grades': {'Computer Science': 87, 'English': 78, 'Art': 90, 'History': 82, 'Economics': 75}
#     },
# ]


def transform_students_dict(students):

    students_list = []

    for name, data in students.items():
        student = {
            'name': name,
            'age': data['age'],
            'subjects': data['subjects'],
            'grades': data['grades']
        }
        students_list.append(student)

    return students_list


# Преобразование
students_list = transform_students_dict(students)

# Вывод результата
print(json.dumps(students_list, indent=4, ensure_ascii=False))


# Задание 6. Сформируйте csv
# Сформируйте файл в формате csv следующего вида
# Заголовки: name,age,grade - имя, возраст и средний балл студента
# Данные:
# John, 20, 85.0
# Alice, 19, 83.3
# Michael, 22, 85.0
# ...


def calculate_average_grade(grades):
    """Вычисляет средний балл по предметам."""
    if not grades:
        return 0.0  # Обработка случая, когда у студента нет оценок
    return sum(grades.values()) / len(grades)

def process_students_data(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            students = json.load(f)
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден.")
        return
    except json.JSONDecodeError:
        print(f"Ошибка: Некорректный формат JSON в файле {input_file}.")
        return

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['name', 'age', 'grade'])

        for name, data in students.items():
            age = data.get('age', '')
            grades = data.get('grades', {})
            average_grade = calculate_average_grade(grades)
            writer.writerow([name, age, f"{average_grade:.1f}"])

    print(f"Данные успешно записаны в файл {output_file}")


input_json_file = 'student_list.json'
output_csv_file = 'student_grades.csv'
process_students_data(input_json_file, output_csv_file)