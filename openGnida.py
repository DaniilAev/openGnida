import os
import shutil
import random
import string

def rand_name():
    return ''.join(random.choices(string.ascii_letters, k=64))

def main():
    volume=32*1024*1024

    print("Создаётся директория для нагрузочных файлов.")

    try:
        os.makedirs('payload',exist_ok=True)

    except Exception as e1:
        print("Не удалось создать директорию для нагрузочных файлов.")
        print(f"Ошибка: {e1}")
        print("Скрипт будет остановлен.")
        exit(1)

    print("Директория создана.")

    while True:
        print(f"Начато заполнение файлами по {volume} байт.")
        volume_filler(volume)
        if volume == 1:
            break
        volume //= 2

    try:
        shutil.rmtree('payload')

    except Exception as e2:
        print("Не удалось удалить директорию для нагрузочных файлов.\nСкрипт будет остановлен.\n ")
        print(f"Ошибка: {e2}")
        print("Убедитесь, что в текущей директории разрешено удаление файлов.")
        print("Скрипт будет остановлен.")
        exit(1)

    print("Директория для нагрузочных файлов удалена, место освобождено.")

    print('Готово.')
    exit(0)


def volume_filler(file_size: int):
    number = 1
    for attempt in range(5):
        try:
            while True:
                with open(f"payload/{rand_name()}.bin", "wb") as file:
                    file.write(b'\xFF'*file_size)
                    file.close()
                number += 1
        except:
            pass

confirm = False
assert confirm

if __name__ == '__main__':
    main()