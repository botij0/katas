def main():
    file_content = read_file("puzzle_input.txt")
    file_array = [list(line) for line in file_content]
    i, j, direction = find_guard(file_array)
    print(f"Guard is at ({i}, {j}) and direction is {direction}")

    coords = set()
    coords.add((i, j))
    while not is_map_limits(file_array, i, j, direction):
        i, j, direction = do_move(file_array, direction, i, j)
        coords.add((i, j))

    print(f"X count: {len(coords)}")


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


def do_move(file_array: list, direction: str, i: int, j: int) -> tuple:
    fi, fj = 0, 0
    if direction == "^":
        if file_array[i - 1][j] == "#":
            fi, fj, direction = do_move(file_array, ">", i, j)
        else:
            fi, fj = i - 1, j

    elif direction == ">":
        if file_array[i][j + 1] == "#":
            fi, fj, direction = do_move(file_array, "v", i, j)
        else:
            fi, fj = i, j + 1

    elif direction == "<":
        if file_array[i][j - 1] == "#":
            fi, fj, direction = do_move(file_array, "^", i, j)
        else:
            fi, fj = i, j - 1

    elif direction == "v":
        if file_array[i + 1][j] == "#":
            fi, fj, direction = do_move(file_array, "<", i, j)
        else:
            fi, fj = i + 1, j

    return fi, fj, direction


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
