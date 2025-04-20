# Задание 0

import csv

data = [
    {'Имя': 'Анна', 'Возраст': '25', 'Город': 'Москва'},
    {'Имя': 'Петр', 'Возраст': '30', 'Город': 'Санкт-Петербург'},
    {'Имя': 'Мария', 'Возраст': '28', 'Город': 'Киев'}
]

# Записываем данные в CSV файл с использованием словаря
with open('данные_с_заголовками.csv', 'w') as csvfile:
    fieldnames = ['Имя', 'Возраст', 'Город']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Записываем заголовки
    writer.writerows(data)  # Записываем данные

# Чтение данных из CSV файла с использованием словаря
with open('данные_с_заголовками.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Имя'], row['Возраст'], row['Город'])

# Задание 1
# Имеется текстовый файл prices.txt с информацией о заказе из интернет магазина.
# В нем каждая строка с помощью символа табуляции \t разделена на три колонки:
# наименование товара; количество товара (целое число); цена (в рублях) товара за 1 шт.
# (целое число). Напишите программу, преобразующую данные из txt в csv.

import csv
# Открываем исходный текстовый файл
with open('prices.txt', 'r', encoding='utf-8') as txt_file:
    # Читаем строки из файла
    lines = txt_file.readlines()

# Открываем CSV файл для записи
with open('prices.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Наименование', 'Количество', 'Цена за 1 шт.'])

    # Обрабатываем каждую строку из текстового файла и разбиваем строку по символу табуляции
    for line in lines:
        columns = line.strip().split('\t')
        # Записываем данные в CSV файл
        writer.writerow(columns)

print("Данные успешно преобразованы из prices.txt в prices.csv")

# Задание 2
# Имеется файл prices.csv (сформированный в прошлом задании) с информацией о заказе из интернет магазина. 
# В нем каждая строка содержит три колонки: наименование товара; количество товара (целое число); цена (в рублях) товара за 1 шт. 
# (целое число). Напишите программу, подсчитывающую общую стоимость заказа.

import csv

total_cost = 0

# Открываем файл prices.csv для чтения
with open('prices.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)

    # Пропускаем заголовок
    next(reader)

    # Обрабатываем каждую строку в CSV файле
    for row in reader:
        if len(row) == 3:
            product_name = row[0]
            quantity = int(row[1])
            price_per_item = int(row[2])
            total_cost += quantity * price_per_item

print(f"Общая стоимость заказа: {total_cost} руб.")
