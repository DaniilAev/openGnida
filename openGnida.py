def main():
    pass

def volume_filler(file_size: int) -> Exception:
    number = 1
    current_exception = None
    for attempt in range(5):
        try:
            while True:
                with open(f"dumb_file{file_size}_{number}.bin", "wb") as file:
                    file.write(b'\xFF'*file_size)
                    file.close()
                number += 1
        except Exception as exp:
            current_exception = exp
    return current_exception




confirm = False
assert confirm

if __name__ == '__main__':
    main()