try:
    with open('sample.txt', 'r') as file:
        print("Reading the file content...")
        lines = file.read()
    print(lines)
except FileNotFoundError:
    print("error: File not found.")
    



