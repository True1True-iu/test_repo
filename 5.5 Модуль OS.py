# Задание: Управление файлами и директориями
# Часть 1: Работа с файлами и директориями
# Создайте программу, которая создаст новую директорию с именем "Управление_файлами".
# В этой директории создайте два файла: "file1.txt" и "file2.txt".
# Запишите в каждый из файлов какой - то текст.
# Выведите содержимое директории на экран.

import os, shutil


def manage_files():
    # 1. Создание новой директории с именем "Управление_файлами".
    # Проверяем, существует ли директория, и создаем её, если не существует

    directory_name = "Управление_файлами"

    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Директория '{directory_name}' успешно создана.")
    else:
        print(f"Директория '{directory_name}' уже существует.")

    # 2. Создание и запись файлов 'file1.txt' и 'file2.txt'
    file1_path = os.path.join(directory_name, "file1.txt")
    file2_path = os.path.join(directory_name, "file2.txt")

    # 3.1 Записываем текст в file1.txt
    with open(file1_path, 'w', encoding='utf-8') as file1:
        file1.write("Здравствуйте.")

    # 3.2 Записываем текст в file2.txt
    with open(file2_path, 'w', encoding='utf-8') as file2:
        file2.write("До свидания.")

    print("Файлы успешно созданы и записаны.")

    # 4. Вывод содержимого директории на экран
    print("\nСодержимое директории:")
    for item in os.listdir(directory_name):
        print(item)

    # Часть 2: Удаление файлов и директории
    # Удалите один из созданных файлов.
    # Создайте еще одну поддиректорию внутри "Управление_файлами".
    # Переместите оставшийся файл в эту новую поддиректорию.
    # Удалите исходную директорию "Управление_файлами" вместе с ее содержимым.

    # 1. Удаляем file2.txt
    os.remove(file2_path)
    print(f"Файл '{file2_path}' удалён.")

    # 2. Создаём ещё одну поддиректорию внутри 'Управление_файлами'
    subdirectory_name = os.path.join(directory_name, "Поддиректория")
    os.makedirs(subdirectory_name, exist_ok=True)
    print(f"Поддиректория '{subdirectory_name}' успешно создана.")

    # 3. Перемещение file1.txt в поддиректорию
    new_file1_path = os.path.join(subdirectory_name, "file1.txt")
    os.rename(file1_path, new_file1_path)
    print(f"Файл '{file1_path}' перемещён в '{subdirectory_name}'.")

    # 4. Удаление исходной директории 'Управление_файлами' вместе с её содержимым
    shutil.rmtree(directory_name)
    print(f"Директория '{directory_name}' успешно удалена.")


manage_files()