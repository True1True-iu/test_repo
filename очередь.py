class Queue:
    def __init__(self):
        self.items = []

    #Добавляем элемент в конец очереди
    def enqueue(self, item):
        self.items.append(item)
    #Извлекаем и возвращаем элемент из начала очереди
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def is_empty(self):
        #проверка на пустоту очереди
        return len(self.items) == 0

    def size(self):
        #получение размера очереди
        return len(self.items)

# Пример использования:
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Размер очереди:", queue.size())  # Размер очереди: 3

    while not queue.is_empty():
        item = queue.dequeue()
        print("Извлечен элемент:", item)