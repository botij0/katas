def main():
    mapp, instructions = read_file("puzzle_input.txt")
    inst_list = list(instructions)
    mapp = mapp.split("\n")
    mapp = [list(map(lambda x: x.strip(), line)) for line in mapp]
    display_map(mapp)
    robot_pos = get_robot_position(mapp)
    for i in range(len(inst_list)):
        if inst_list[i] == "\n":
            continue
        mapp, robot_pos = do_instruction(mapp, inst_list[i], robot_pos)

    display_map(mapp)
    print(get_sum_gps_coords(mapp))


def get_sum_gps_coords(mapp):
    total = 0
    for i in range(len(mapp)):
        for j in range(len(mapp[i])):
            if mapp[i][j] == "O":
                total += 100 * i + j
    return total


def get_robot_position(mapp):
    for i in range(len(mapp)):
        for j in range(len(mapp[i])):
            if mapp[i][j] == "@":
                return i, j
    return None, None


def display_map(mapp):
    for i in range(len(mapp)):
        for j in range(len(mapp[i])):
            print(mapp[i][j], end="")
        print()
    print()


def do_instruction(mapp, inst, robot_pos):
    i, j = robot_pos
    if inst == ">":
        if mapp[i][j + 1] == "#":
            return mapp, robot_pos
        elif mapp[i][j + 1] == ".":
            mapp[i][j + 1] = "@"
            mapp[i][j] = "."
            return mapp, (i, j + 1)
        else:
            f_space = find_right_row_free_space(mapp, i, j)
            if f_space is not None:
                aux = j + 2
                while aux <= f_space:
                    mapp[i][aux] = "O"
                    aux += 1
                mapp[i][j + 1] = "@"
                mapp[i][j] = "."
                return mapp, (i, j + 1)
            else:
                return mapp, robot_pos
    elif inst == "<":
        if mapp[i][j - 1] == "#":
            return mapp, robot_pos
        elif mapp[i][j - 1] == ".":
            mapp[i][j - 1] = "@"
            mapp[i][j] = "."
            return mapp, (i, j - 1)
        else:
            f_space = find_left_row_free_space(mapp, i, j)
            if f_space is not None:
                aux = j - 2
                while aux >= f_space:
                    mapp[i][aux] = "O"
                    aux -= 1
                mapp[i][j - 1] = "@"
                mapp[i][j] = "."
                return mapp, (i, j - 1)
            else:
                return mapp, robot_pos
    elif inst == "v":
        if mapp[i + 1][j] == "#":
            return mapp, robot_pos
        elif mapp[i + 1][j] == ".":
            mapp[i + 1][j] = "@"
            mapp[i][j] = "."
            return mapp, (i + 1, j)
        else:
            f_space = find_down_col_free_space(mapp, j, i)
            if f_space is not None:
                aux = i + 2
                while aux <= f_space:
                    mapp[aux][j] = "O"
                    aux += 1
                mapp[i + 1][j] = "@"
                mapp[i][j] = "."
                return mapp, (i + 1, j)
            else:
                return mapp, robot_pos
    elif inst == "^":
        if mapp[i - 1][j] == "#":
            return mapp, robot_pos
        elif mapp[i - 1][j] == ".":
            mapp[i - 1][j] = "@"
            mapp[i][j] = "."
            return mapp, (i - 1, j)
        else:
            f_space = find_up_col_free_space(mapp, j, i)
            if f_space is not None:
                aux = i - 2
                while aux >= f_space:
                    mapp[aux][j] = "O"
                    aux -= 1
                mapp[i - 1][j] = "@"
                mapp[i][j] = "."
                return mapp, (i - 1, j)
            else:
                return mapp, robot_pos


def find_right_row_free_space(mapp, row, start_col):
    for i in range(start_col, len(mapp[row])):
        if mapp[row][i] == "#":
            break
        elif mapp[row][i] == ".":
            return i
    return None


def find_left_row_free_space(mapp, row, start_col):
    for i in range(start_col, 0, -1):
        if mapp[row][i] == "#":
            break
        elif mapp[row][i] == ".":
            return i
    return None


def find_down_col_free_space(mapp, col, start_row):
    for i in range(start_row, len(mapp)):
        if mapp[i][col] == "#":
            break
        elif mapp[i][col] == ".":
            return i
    return None


def find_up_col_free_space(mapp, col, start_row):
    for i in range(start_row, 0, -1):
        if mapp[i][col] == "#":
            break
        elif mapp[i][col] == ".":
            return i
    return None


def read_file(filename):
    with open(filename) as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    main()
