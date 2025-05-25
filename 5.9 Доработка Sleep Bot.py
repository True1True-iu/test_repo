import telebot
import os
import datetime
import json

token = os.getenv('TG_TOKEN')
bot = telebot.TeleBot(token)

# Загружаем данные из файла sleep_data.json при запуске бота
def load_sleep_data():
    try:
        with open('sleep_data.json', 'r') as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Загружаем существующие данные о сне при запуске бота
sleep_data = load_sleep_data()
users = {}


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id,
                     'Привет! Я буду помогать тебе отслеживать количество сна.\n'
                     'Используй команду /sleep для того, чтобы отметить время начала твоего сна,\n'
                     'а так же команду /wake, чтобы указать время его окончания.')


# @bot.message_handler(commands=['sleep'])
# def sleep(message):
#     user_id = message.from_user.id
#     users[user_id] = {'start_time': datetime.datetime.now()}
#     bot.send_message(message.chat.id, "Отметил начало сна.")
@bot.message_handler(commands=['sleep'])
def sleep(message):
    user_id = message.from_user.id
    if user_id not in users:
        users[user_id] = {}
        users[user_id]['start_time'] = datetime.datetime.now()

@bot.message_handler(commands=['wake'])
def wake(message):
    user_id = message.from_user.id
    if user_id not in users or 'start_time' not in users[user_id]:
        bot.send_message(message.chat.id, "Вы не отметили время засыпания.")
        return

    end_time = datetime.datetime.now()
    start_time = users[user_id]['start_time']
    duration = (end_time - start_time).total_seconds()


    sleep_record = {
        'user_id': user_id,
        'start_time': start_time.isoformat(),
        'end_time': end_time.isoformat(),
        'duration': duration
    }

    sleep_data.append(sleep_record)

    try:
        with open('sleep_data.json', 'w') as f:  # Перезаписываем файл целиком
            json.dump(sleep_data, f, indent=2)
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

    bot.send_message(message.chat.id,
                     f"Вы спали {duration} секунд.")


bot.polling()
