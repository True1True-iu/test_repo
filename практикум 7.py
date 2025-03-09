from dataclasses import dataclass
#Создайте класс Student с полями: name (имя студента), age (возраст студента), major (специальность) и gpa (средний балл студента).

@dataclass
class Student:
    name: str
    age: int
    major: str
    gpa: float

# Реализуйте метод display_info(self), который выводит информацию о студенте в удобном формате.

    def display_info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Специальность: {self.major}")
        print(f"Средний балл студента: {self.gpa}")

    def calculate_grade(self):
        if self.gpa >= 4.0:
            return "Отлично"
        elif self.gpa >= 3.0:
            return "Хорошо"
        elif self.gpa >= 2.0:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"

# Создание списка студентов
students = [
    Student("Alice", 20, "Computer Science", 3.8),
    Student("Bob", 22, "Engineering", 3.2),
    Student("Charlie", 21, "Mathematics", 4.5),
    Student("David", 23, "Physics", 2.7),
    Student("Eve", 19, "Biology", 3.9),
]

# Отображение информации о студентах
for student in students:
    student.display_info()

# Сравнение студентов
print("Are Alice and Bob the same student?", students[0] == students[1])
print("Are Alice and Eve the same student?", students[0] == students[4])

# Расчет и вывод оценок
for student in students:
    print(f"{student.name} - Grade: {student.calculate_grade()}")