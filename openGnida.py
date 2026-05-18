import os
import shutil

def main():
    volume=32*1024*1024
    os.makedirs('payload',exist_ok=True)
    while True:
        print(f"Начато заполнение файлами по {volume} байт.")
        volume_filler(volume)
        if volume == 1:
            break
        volume //= 2
    print('Готово.')


def volume_filler(file_size: int):
    number = 1
    for attempt in range(5):
        try:
            while True:
                with open(f"payload/dumb_file{file_size}_{number}.bin", "wb") as file:
                    file.write(b'\xFF'*file_size)
                    file.close()
                number += 1
        except:
            pass

confirm = False
assert confirm

if __name__ == '__main__':
    main()