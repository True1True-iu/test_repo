# Реализовать конвертер из csv в json формат:
# [{column -> value}, ... , {column -> value}]
# название столбца — значение (аналог DictReader из модуля csv).
# Для csv формата принять
# разделитель между значениями, по умолчанию ","
# разделитель строк, по умолчанию "\n".
#  В результате распечатать json строку с отступами равными 4.


import csv
import json

def csv_to_json(csv_file_path, delimiter=','):
    data = []

    # Открываем CSV файл
    with open('prices.csv', 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)

        for row in reader:
            data.append(row)

    # Конвертируем список в JSON формат
    json_output = json.dumps(data, indent=4,ensure_ascii=False)
    print(json_output)

# Открываем исходный CSV файл и выводим его содержимое в формате JSON
csv_to_json('prices.csv')