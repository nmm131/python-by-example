# 15_file_io - Python by Example

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def main():
    file_name = "data/sample.txt"
    write_file(file_name, "This is a test.\nHello, file!")
    content = read_file(file_name)
    print("File contents:")
    print(content)

if __name__ == "__main__":
    main()
