def main():
    file_content = read_file("puzzle_input.txt")
    file_array = [list(line) for line in file_content]
    i, j, direction = find_guard(file_array)
    print(f"Guard is at ({i}, {j}) and direction is {direction}")

    while not is_map_limits(file_array, i, j, direction):
        file_array = do_move(file_array, direction, i, j)
        i, j, direction = find_guard(file_array)

    x_count = 1
    for line in file_array:
        print("".join(line))
        x_count += line.count("X")

    print(f"X count: {x_count}")


def find_guard(file_array: list) -> tuple:
    for i in range(len(file_array)):
        for j in range(len(file_array[i])):
            if file_array[i][j] in ["^", ">", "<", "v"]:
                return (i, j, file_array[i][j])


def is_map_limits(file_array: list, i: int, j: int, direction: str) -> bool:
    if direction == "^":
        if i == 0:
            return True
    elif direction == ">":
        if j == len(file_array[0]) - 1:
            return True
    elif direction == "<":
        if j == 0:
            return True
    elif direction == "v":
        if i == len(file_array) - 1:
            return True

    return False


def do_move(file_array: list, direction: str, i: int, j: int) -> list:
    if direction == "^":
        if file_array[i - 1][j] == "#":
            do_move(file_array, ">", i, j)
        else:
            file_array[i - 1][j] = "^"
            file_array[i][j] = "X"

    elif direction == ">":
        if file_array[i][j + 1] == "#":
            do_move(file_array, "v", i, j)
        else:
            file_array[i][j + 1] = ">"
            file_array[i][j] = "X"

    elif direction == "<":
        if file_array[i][j - 1] == "#":
            do_move(file_array, "^", i, j)
        else:
            file_array[i][j - 1] = "<"
            file_array[i][j] = "X"

    elif direction == "v":
        if file_array[i + 1][j] == "#":
            do_move(file_array, "<", i, j)
        else:
            file_array[i + 1][j] = "v"
            file_array[i][j] = "X"

    return file_array


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
