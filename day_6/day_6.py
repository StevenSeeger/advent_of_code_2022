FILENAME = "input.txt"

def process_file(filename):
    with open(filename) as f:
        message = f.read()
        for i in range(len(message)):
            marker = set(message[i:i+4])
            if len(marker) == 4:
                print(marker)
                print(i+4)
                break

    with open(filename) as f:
        message = f.read()
        for i in range(len(message)):
            marker = set(message[i:i+14])
            if len(marker) == 14:
                print(marker)
                print(i+14)
                break

if __name__ == "__main__":
    process_file(FILENAME)