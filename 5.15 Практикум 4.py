# 1. Дан словарь учеников. Отсортировать учеников по возрасту.

students_dict = {
 'Саша': 27,
 'Кирилл': 52,
 'Маша': 14,
 'Петя': 36,
 'Оля': 43,
}

sorted_people = sorted(students_dict.items(), key=lambda x: x[1])
print(sorted_people)


# 2. Дан список с данными о росте и весе людей. Отсортировать их по индексу массы тела.
# Он вычисляется по формуле: Вес тела в килограммах/(Рост в метрах∗Рост в метрах)

data = [
    (82, 191),
    (68, 174),
    (90, 189),
    (73, 179),
    (76, 184)
]

# Функция для расчёта индекса массы тела
def calculate_bmi(weight, height):
    height_in_meters = height / 100  # Преобразуем высоту в метры
    return weight / (height_in_meters ** 2)

sorted_data = sorted(data, key=lambda x: calculate_bmi(x[0], x[1]))

for weight, height in sorted_data:
    bmi = calculate_bmi(weight, height)
    print(f"Вес: {weight} кг, Рост: {height} см, индекс массы тела: {bmi:.2f}")


# 3. Дан словарь учеников. Найти самого минимального ученика по возрасту.

students_list = [
    {
        "name": "Саша",
        "age": 27,
    },
    {
        "name": "Кирилл",
        "age": 52,
    },
    {
        "name": "Маша",
        "age": 14,
    },
    {
        "name": "Петя",
        "age": 36,
    },
    {
        "name": "Оля",
        "age": 43,
    },
]

youngest_student = min(students_list, key=lambda student: student['age'])
print(f"Самый младший ученик: {youngest_student['name']}, возраст: {youngest_student['age']}")