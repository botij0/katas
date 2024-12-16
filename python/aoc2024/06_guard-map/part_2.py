def main():
    file_content = read_file("example.txt")
    file_array = [list(line) for line in file_content]

    i, j, direction = find_guard(file_array)
    print(f"Guard is at ({i}, {j}) and direction is {direction}")

    obs_loop = 0
    while not is_map_limits(file_array, i, j, direction):
        if check_loop(file_array, i, j, direction):
            obs_loop += 1

        i, j, direction = do_move(file_array, direction, i, j)

    print(i, j)
    print(f"Obstacle loop count: {obs_loop}")


def check_loop(file_array: list, i: int, j: int, direction: str) -> bool:
    oi, oj = get_next_obstacle(i, j, direction, file_array)
    ii, jj, _ = find_guard(file_array)
    if (ii == oi and jj == oj) or (oi == -1 and oj == -1):
        return False

    visited = set()
    file_array[oi][oj] = "O"

    while not is_map_limits(file_array, i, j, direction):
        if (i, j, direction) in visited:
            file_array[oi][oj] = "."
            return True

        visited.add((i, j, direction))
        i, j, direction = do_move(file_array, direction, i, j)

    file_array[oi][oj] = "."
    return False


def get_next_obstacle(i: int, j: int, direction: str, file_array: list) -> tuple:
    if direction == "^":
        if file_array[i - 1][j] != "#":
            return (i - 1, j)
    elif direction == ">":
        if file_array[i][j + 1] != "#":
            return (i, j + 1)
    elif direction == "<":
        if file_array[i][j - 1] != "#":
            return (i, j - 1)
    elif direction == "v":
        if file_array[i + 1][j] != "#":
            return (i + 1, j)
    return -1, -1


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
        if file_array[i - 1][j] == "#" or file_array[i - 1][j] == "O":
            fi, fj, direction = do_move(file_array, ">", i, j)
        else:
            fi, fj = i - 1, j

    elif direction == ">":
        if file_array[i][j + 1] == "#" or file_array[i][j + 1] == "O":
            fi, fj, direction = do_move(file_array, "v", i, j)
        else:
            fi, fj = i, j + 1

    elif direction == "<":
        if file_array[i][j - 1] == "#" or file_array[i][j - 1] == "O":
            fi, fj, direction = do_move(file_array, "^", i, j)
        else:
            fi, fj = i, j - 1

    elif direction == "v":
        if file_array[i + 1][j] == "#" or file_array[i + 1][j] == "O":
            fi, fj, direction = do_move(file_array, "<", i, j)
        else:
            fi, fj = i + 1, j

    return fi, fj, direction


def display_map(file_array: list) -> None:
    for line in file_array:
        print("".join(line))
    print()


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
