def main():
    file_content = read_file("example.txt")
    numbers = get_numbers_map(file_content)
    display_numbers_map(numbers)

    tree = build_tree(numbers)
    print(tree)


def build_tree(numbers_map: list, target=0) -> dict:
    partial_tree = {}
    for i, line in enumerate(numbers_map):
        for j, number in enumerate(line):
            if number == target and target != 9:
                partial_tree[i, j] = get_next_pos((i, j), 1, numbers_map)
            elif number == target and target == 9:
                partial_tree[i, j] = 0

    if target == 9:
        return partial_tree

    next_tree = build_tree(numbers_map, target + 1)
    return partial_tree | next_tree


def get_next_pos(init_pos: tuple, target: int, number_map: list) -> list:
    routes = {}
    i, j = init_pos
    if i < len(number_map) - 1 and number_map[i + 1][j] == target:
        routes[i + 1, j] = 1
    elif i > 0 and number_map[i - 1][j] == target:
        routes[i - 1, j] = 1
    elif j < len(number_map[i]) - 1 and number_map[i][j + 1] == target:
        routes[i, j + 1] = 1
    elif j > 0 and number_map[i][j - 1] == target:
        routes[i, j - 1] = 1
    return routes


def read_file(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().split("\n")


def get_numbers_map(file_content: list) -> list:
    numbers_map = []
    for line in file_content:
        numbers_map.append([int(x) for x in line])
    return numbers_map


def display_numbers_map(numbers_map: list):
    for line in numbers_map:
        print("".join(str(x) for x in line))


if __name__ == "__main__":
    main()
