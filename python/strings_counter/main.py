import re


def main():
    lines = read_file("puzzle_input.txt")
    memory_len = 0
    literal_len = 0
    for line in lines:
        literal_len += len(line)
        aux = line.encode("utf-8").decode("unicode-escape")
        memory_len += len(aux)-2

    
    print(literal_len)
    print(memory_len)
    print("Resultado: " + str(literal_len- memory_len))


def read_file(file_name: str) -> list:
    with open(file_name, "r") as f:
        return f.read().split()
    

if __name__ == "__main__":
    main()
