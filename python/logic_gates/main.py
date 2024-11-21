def main():
    file_content = read_file("puzzle_input.txt")
    content = file_content.split("\n")
    wires = {"b": 46065}
    while len(wires) < len(content):
        for row in content:
            aux = row.split(" ")
            if len(aux) == 3:
                val = get_value(aux[0], wires)
                if val != -1 and aux[-1] not in wires:
                    wires[aux[-1]] = val
            elif len(aux) == 4:
                val = get_value(aux[1], wires)
                if val != -1:
                    wires[aux[-1]] = not_gate(val)

            else:
                val_1 = get_value(aux[0], wires)
                val_2 = get_value(aux[2], wires)
                if val_1 != -1 and val_2 != -1:
                    match aux[1]:
                        case "AND":
                            wires[aux[-1]] = and_gate(val_1, val_2)

                        case "OR":
                            wires[aux[-1]] = or_gate(val_1, val_2)

                        case "LSHIFT":
                            wires[aux[-1]] = lshift_gate(val_1, val_2)

                        case "RSHIFT":
                            wires[aux[-1]] = rshift_gate(val_1, val_2)

    print(len(wires))
    print(wires)


def get_value(s: str, wires: dict) -> int:
    if is_int(s):
        return int(s)
    elif s in wires:
        return wires[s]
    else:
        return -1


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def not_gate(x: int):
    mask = (1 << 16) - 1
    return ~x & mask


def and_gate(a: str, b: str):
    return a & b


def or_gate(a: str, b: str):
    return a | b


def lshift_gate(a: str, count: int):
    return a << count


def rshift_gate(a: str, count: int):
    return a >> count


def is_int(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


# def rshift_gate(a: str, count: int):


if __name__ == "__main__":
    main()
