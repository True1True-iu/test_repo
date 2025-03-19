class Task:
    def __init__(self, name):
        self.name = name

class TaskQueue:
    def __init__(self):
        # Инициализация очереди задач, представляющей собой список
        self.tasks = []

    def add_task(self, task):
        # Добавление задачи в конец очереди
        self.tasks.append(task)

    def get_next_task(self):
        # Извлечение и возвращение следующей задачи из начала очереди
        if self.is_empty():
            return None
        return self.tasks.pop(0)

    def is_empty(self):
        # Проверка, пуста ли очередь
        return len(self.tasks) == 0

# Пример использования:
if __name__ == "__main__":
    queue = TaskQueue()

    task1 = Task("Задача 1")
    task2 = Task("Задача 2")
    task3 = Task("Задача 3")

    queue.add_task(task1)
    queue.add_task(task2)
    queue.add_task(task3)

    next_task = queue.get_next_task()
    print(f"Следующая задача: {next_task.name if next_task else 'Нет задач'}")  # Ожидаемый результат: "Задача 1"

    queue.get_next_task()  # Извлечь следующую задачу

    print(f"Очередь пуста: {queue.is_empty()}")  # Ожидаемый результат: False

