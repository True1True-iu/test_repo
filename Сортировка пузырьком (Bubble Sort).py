def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for h in range(0, n - i - 1):
            #сравниваем соседние элементы
            if arr[h] > arr[h + 1]:
                #меняем их местами, если они находятся в неправильном порядке
                arr[h], arr[h + 1] = arr[h + 1], arr[h]

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Отсортированный список:", my_list)