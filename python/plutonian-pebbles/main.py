def main():
    file_content = read_file("example.txt")
    print(file_content)


def read_file(filename: str):
    with open(filename) as f:
        return f.read()


if __name__ == "__main__":
    main()
