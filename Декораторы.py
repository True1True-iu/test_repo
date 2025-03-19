# Задание 1. Измерьте с помощью декоратора measure_execution_time продолжительность HTTP запроса
# к произвольному url (можно взять код из первых уроков по ботам)

import requests
from datetime import datetime

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        t_start = datetime.now()
        result = func(*args, **kwargs)
        t_finish = datetime.now()
        execution_time = t_finish - t_start
        milliseconds = round(execution_time.microseconds / 1000)
        print(f"Запрос выполнен за "
              f"{execution_time.seconds}сек {milliseconds}мс")
        return result
    return wrapper

@measure_execution_time
def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status() # Проверяем статус ответа
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")


if __name__ == "__main__":
    url1 = "https://www.google.com"
    response_content = make_request(url1)

# Задание 2. Необходимо разработать декоратор requires_admin, который будет использоваться для
# проверки роли пользователя перед выполнением защищенной функции. Если роль пользователя не
# соответствует требуемой, декоратор должен выбрасывать исключение PermissionError. В противном
# случае функция должна выполняться корректно.

def requires_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.get('role') != 'admin':
            raise PermissionError("У вас нет прав для выполнения этой операции.")
        return func(user, *args, **kwargs)
    return wrapper

@requires_admin
def delete_user(user, username_to_delete):
    return f"Пользователь {username_to_delete} был удалён {user['username']}."

# Пример юзеров
admin_user = {'username': 'Alice', 'role': 'admin'}
regular_user = {'username': 'Bob', 'role': 'user'}

# Вызовы функции
try:
    print(delete_user(admin_user, 'Charlie'))  # Должно отработать
except PermissionError as e:
    print(e)

try:
    print(delete_user(regular_user, 'Charlie'))  # Должно рейзить PermissionError
except PermissionError as e:
    print(e)
