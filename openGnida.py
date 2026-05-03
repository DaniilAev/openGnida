def main():
    volume=32
    while True:
        volume_filler(volume)
        if volume == 1:
            break
        volume //= 2

def volume_filler(file_size: int) -> bool:
    number = 1
    is_exception_raised = False
    for attempt in range(5):
        try:
            while True:
                with open(f"dumb_file{file_size}_{number}.bin", "wb") as file:
                    file.write(b'\xFF'*file_size)
                    file.close()
                number += 1
        except OSError:
            is_exception_raised = True
    return is_exception_raised


confirm = False
assert confirm

if __name__ == '__main__':
    main()