def main():
    file_content = read_file("puzzle_input.txt")
    numbers = get_numbers_map(file_content)
    display_numbers_map(numbers)

    build_tree(numbers)


def build_tree(numbers_map: list) -> dict:
    tree = {}
    score = 0

    for i, line in enumerate(numbers_map):
        for j, number in enumerate(line):
            if number == 0:
                results = set()
                tree[i, j] = get_branches((i, j), 1, numbers_map, results)
                score += len(results)

    print(score)
    return tree


def get_branches(parent: tuple, target: int, number_map: list, results: set) -> dict:
    branches = {}
    if target >= 10:
        results.add(parent)
        return branches
    i, j = parent
    if i < len(number_map) - 1 and number_map[i + 1][j] == target:
        branches[i + 1, j] = get_branches((i + 1, j), target + 1, number_map, results)
    if i > 0 and number_map[i - 1][j] == target:
        branches[i - 1, j] = get_branches((i - 1, j), target + 1, number_map, results)
    if j < len(number_map[i]) - 1 and number_map[i][j + 1] == target:
        branches[i, j + 1] = get_branches((i, j + 1), target + 1, number_map, results)
    if j > 0 and number_map[i][j - 1] == target:
        branches[i, j - 1] = get_branches((i, j - 1), target + 1, number_map, results)
    return branches


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
