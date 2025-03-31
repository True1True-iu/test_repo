def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        #находим минимальный элемент
        min_index = i
        for h in range(i + 1, n):
            if arr[h] < arr[min_index]:
                min_index = h
        #меняем минимальный элемент с элементом на текущей позиции
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print("Отсортированный список:", my_list)