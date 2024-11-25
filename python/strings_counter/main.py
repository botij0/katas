import re


def main():
    lines = read_file("example.txt")
    memory_len = 0
    literal_len = 0
    part_2mem = 0
    for line in lines:
        print(line)
        literal_len += len(line)
        part_2mem += get_memory_len_2(line)
        aux = line.encode("utf-8").decode("unicode-escape")
        memory_len += len(aux)-2

    
    # print("Resultado: " + str(literal_len- memory_len))
    print(len(lines[3]))
    print(get_memory_len_2(lines[3]))
    print("Resultado parte 2: " + str(part_2mem-literal_len))

# Part 2
# " -> "\"
# \ -> \\\
# \xHH -> \\xHH




def get_memory_len_2(line: str) -> int:
    return len(re.sub('"', '"\"', repr(line)))

def read_file(file_name: str) -> list:
    with open(file_name, "r") as f:
        return f.read().split()
    

if __name__ == "__main__":
    main()
