def main():
    # x = 123
    # y = 456
    # print(x & y)
    # # d = bin(x) and bin(y)
    # # print(int(d, 2))
    # print(bin(x & y))
    # and_gate(format(x, "016b"), format(y, "016b"))
    # or_gate(format(x, "016b"), format(y, "016b"))
    # lshift_gate(format(x, "016b"), 2)
    file_content = read_file("example_input.txt")
    content = file_content.split("\n")
    wires = {}
    for row in content:
        aux = row.split(" ")
        if len(aux) == 3:
            wires[aux[-1]] = int(aux[0])
        elif len(aux) == 4:
            wires[aux[-1]] = not_gate(wires[aux[1]])
    print(wires)


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def not_gate(x: int):
    mask = (1 << 16) - 1
    return ~x & mask


def and_gate(a: str, b: str):
    r_value = ""
    min_len = len(a) if len(a) < len(b) else len(b)
    for i in range(0, min_len):
        if int(a[i]) and int(b[i]):
            r_value += "1"
        else:
            r_value += "0"

    print(r_value)
    print(int(r_value, 2))


def or_gate(a: str, b: str):
    r_value = ""
    min_len = len(a) if len(a) < len(b) else len(b)
    for i in range(0, min_len):
        if int(a[i]) or int(b[i]):
            r_value += "1"
        else:
            r_value += "0"

    print(r_value)
    print(int(r_value, 2))


def lshift_gate(a: str, count: int):
    aux = int(a, 2)
    aux = aux << count
    print(aux)
    print(format(aux, "016b"))


def rshift_gate(a: str, count: int):
    aux = int(a, 2)
    aux = aux >> count
    print(aux)
    print(format(aux, "016b"))


# def rshift_gate(a: str, count: int):


if __name__ == "__main__":
    main()
