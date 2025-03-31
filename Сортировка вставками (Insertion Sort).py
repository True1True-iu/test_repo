def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i
        #перемещаем элементы, которые больше текущего, на одну позицию вправо
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]  #сдвигаем элемент вправо
            position -= 1  # переходим к предыдущему элементу
        #вставляем текущий элемент на его позицию
        arr[position] = current_value

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)
print("Отсортированный список:", my_list)