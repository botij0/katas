def main():
    file_content = read_file("puzzle_input.txt")
    col1, col2 = get_columns(file_content)
    print(get_distance(col1, col2))
    print(get_distance_pt2(col1, col2))


def get_columns(n_list: list) -> tuple:
    col1 = []
    col2 = []
    for i, val in enumerate(n_list):
        if i % 2 == 0:
            col1.append(val)
        else:
            col2.append(val)

    return sorted(col1), sorted(col2)


def get_distance(col1: list, col2: list) -> int:
    total = 0
    for i in range(0, len(col1)):
        if col2[i] >= col1[i]:
            total += col2[i] - col1[i]
        else:
            total += col1[i] - col2[i]

    return total


def get_distance_pt2(col1: list, col2: list) -> int:
    total = 0
    for i in range(0, len(col1)):
        total += col1[i] * col2.count(col1[i])
    return total


def read_file(filename: str) -> list:
    with open(filename) as f:
        return [int(x) for x in f.read().split()]


if __name__ == "__main__":
    main()
