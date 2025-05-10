#Задание 1: Работа с JSON файлом
# Задача:
# Студентам предлагается JSON файл с данными о студентах. Необходимо создать программу,
# которая проведет анализ этих данных и выведет информацию на экран.
# Прочитать данные из файла students.json.
# Определить общее количество студентов в файле.
# Найти студента с самым высоким возрастом и вывести его данные (имя, возраст, город).
# Определить количество студентов, изучающих определенный предмет (например, Python).

import json

# 1. Читаем данные из файла students.json
with open('students.json', 'r', encoding='utf-8') as file:
    students = json.load(file)

# 2. Определяем общее количество студентов
total_students = len(students)
print(f"Общее количество студентов: {total_students}")

# 3. Находим студента с самым высоким возрастом и выводим его данные (имя, возраст, город).
oldest_student = students[0]
for student in students:
    if student['возраст'] > oldest_student['возраст']:
        oldest_student = student

print("Самый старший студент:")
print(f"Имя: {oldest_student['имя']}, Возраст: {oldest_student['возраст']}, Город: {oldest_student['город']}")

# 4. Определяем количество студентов, изучающих Python
python_students_count = 0
for student in students:
    if 'Python' in student.get('предметы', []):
        python_students_count += 1

print(f"Количество студентов, изучающих Python: {python_students_count}")

# Задание 2: Работа с CSV файлом
# Задача:
# Предоставить студентам файл в формате CSV с данными о продажах в компании.
# Задача - обработать этот файл и получить полезную информацию.
# Считать данные из файла sales.csv.
# Подсчитать общую сумму продаж за весь период.
# Определить продукт с самым высоким объемом продаж и вывести его на экран.
# Разделить данные на категории по месяцам и вывести общую сумму продаж для каждого месяца.

import csv
from datetime import datetime

def analyze_sales(file_path):
    total_sales = 0.0
    product_sales = {}
    monthly_sales = {}

    # 1. Считываем данные из файла sales.csv.
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader((line.strip() for line in csv_file), skipinitialspace=True)

        for row in reader:
            date_str = row['Дата'].strip()
            product = row['Продукт'].strip()
            sales_amount = float(row['Сумма'].strip())

            date = datetime.strptime(date_str, '%Y-%m-%d')

            # 2. Подсчитываем общую сумму продаж за весь период.
            total_sales += sales_amount

            # Делаем подсчет по продуктам
            product_sales[product] = product_sales.get(product, 0) + sales_amount

            # 4. Разделяем данные на категории по месяцам.
            month_year = date.strftime('%Y-%m')
            monthly_sales[month_year] = monthly_sales.get(month_year, 0) + sales_amount

    # 3. Определяем продукт с самым высоким объемом продаж без использования lambda
    best_selling_product = None
    highest_sales_amount = 0

    for product, sales in product_sales.items():
        if sales > highest_sales_amount:
            best_selling_product = product
            highest_sales_amount = sales

    print(f"\nОбщая сумма продаж: {total_sales:.2f}")
    if best_selling_product:
        print(f"Продукт с самым высоким объемом продаж: {best_selling_product}, Сумма: {highest_sales_amount:.2f}")

    print("\nОбщая сумма продаж по месяцам:")
    for month in sorted(monthly_sales.keys()):
        print(f"{month}: {monthly_sales[month]:.2f}")

analyze_sales('sales.csv')

# Задание 3: Комбинированная работа с JSON и CSV
# Задача:
# Предоставить студентам два файла - JSON с информацией о сотрудниках и CSV с данными о их
# производительности. Задача - соединить эти данные для анализа.
# Считать данные из файлов employees.json и performance.csv.
# Сопоставить данные о производительности каждого сотрудника с их соответствующей информацией из JSON файла.
# Определить среднюю производительность среди всех сотрудников и вывести ее.
# Найти сотрудника с наивысшей производительностью и вывести его имя и показатель производительности.

import json
import csv

def analyze_employee_performance():
    # 1. Считываем данные из файла employees.json
    employees = []

    with open('employees.json', 'r', encoding='utf-8') as json_file:
        employees = json.load(json_file)

    # 2.  Считываем данные из файла performance.csv.
    performance_data = {}

    with open('performance.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Конвертация полей employee_id и performance в целые числа
            employee_id = int(row['employee_id'])
            performance = int(row['performance'])
            performance_data[employee_id] = performance


    # 3. Сопоставляем данные о производительности каждого сотрудника с их соответствующей информацией из JSON файла
    combined_data = []
    for employee in employees:
        emp_id = employee['id']
        if emp_id in performance_data:
            combined_data.append({
                'id': emp_id,
                'имя': employee['имя'],
                'должность': employee['должность'],
                'производительность': performance_data[emp_id]
            })

    if not combined_data:
        print("Нет данных для анализа!")
        return

    # 4. Определяем среднюю производительность среди всех сотрудников и вывести ее
    total_performance = sum(emp['производительность'] for emp in combined_data)
    average_performance = total_performance / len(combined_data)
    print(f"Средняя производительность всех сотрудников: {average_performance:.1f}%")

    # 5. Находим сотрудника с наивысшей производительностью и выводим его имя и показатель производительности.
    best_employee = None
    highest_performance = -1

    for emp in combined_data:
        if emp['производительность'] > highest_performance:
            highest_performance = emp['производительность']
            best_employee = emp

    print(f"\nСотрудник с наивысшей производительностью:")
    if best_employee:
        print(f"Имя: {best_employee['имя']}")
        print(f"Производительность: {best_employee['производительность']}%")
    else:
        print("Нет сотрудников с производительностью.")

analyze_employee_performance()