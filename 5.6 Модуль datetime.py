# Часть 1: Работа с текущей датой и временем
# Получите текущую дату и время.
# Выведите на экран день недели для этой даты.
# Определите, является ли год текущей даты високосным, и выведите соответствующее сообщение.

import datetime
import locale

def current_date_time_info():
    locale.setlocale(locale.LC_TIME, 'russian')
    # Получаем текущую дату и время
    now = datetime.datetime.now()

    # Выводим на экран день недели
    day_of_week = now.strftime("%A")
    print(f"Сегодня: {now.strftime('%Y-%m-%d %H:%M:%S')}, день недели: {day_of_week}")

    # Определяем, является ли год високосным
    type_of_year = (now.year % 4 == 0 and now.year % 100 != 0) or (now.year % 400 == 0)
    if type_of_year:
        print(f"{now.year} год является високосным.")
    else:
        print(f"{now.year} год не является високосным.")

current_date_time_info()

# Часть 2: Работа с пользовательской датой
# Запросите у пользователя ввод даты в формате "год-месяц-день" (например, "2023-12-31").
# Определите, сколько дней осталось до введенной даты от текущей даты.
# Рассчитайте разницу между этими двумя датами и выведите результат в формате дней, часов и минут.

def user_date_info():
    locale.setlocale(locale.LC_TIME, 'russian')
    # Запрашиваем у пользователя ввод даты
    user_date_input = input("Введите дату в формате 'год-месяц-день' (например, '2023-12-31'): ")

    try:
        # Парсинг пользовательского ввода в объект datetime
        user_date = datetime.datetime.strptime(user_date_input, '%Y-%m-%d')

        # Получаем текущую дату
        now = datetime.datetime.now()

        # Рассчитаем разницу между двумя датами и выводим результат в формате дней, часов и минут.
        difference = user_date - now
        days = difference.days
        total_seconds = difference.total_seconds()
        hours, remainder = divmod(total_seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        # Выводим результат
        if days >= 0:
            print(f"Осталось {days} дней, {int(hours)} часов и {int(minutes)} минут до {user_date_input}.")
        else:
            print(f"Дата {user_date_input} уже прошла.")

    except ValueError:
        print("Неверный формат даты. Пожалуйста, используйте формат 'год-месяц-день'.")

user_date_info()