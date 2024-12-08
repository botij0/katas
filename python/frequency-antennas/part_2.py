def main():
    file_content = read_file("puzzle_input.txt")
    mapp = [[c for c in line] for line in file_content.splitlines()]
    antennas = get_antennas_dict(file_content, mapp)
    antennas_dict = calculate_distances(antennas)
    antinode_count = put_antinode(antennas_dict, mapp)

    display_map(mapp)
    print(antinode_count)


def put_antinode(antennas_dict: dict, mapp: list) -> int:
    count = 0
    for _, positions in antennas_dict.items():
        for base, relatives in positions.items():
            for relative in relatives:
                i, j = base
                i2, j2 = relative
                while check_valid_position(i, i2, j, j2, mapp):
                    if mapp[i + i2][j + j2] == ".":
                        mapp[i + i2][j + j2] = "#"
                        count += 1
                    i, j = i + i2, j + j2
            count += 1
    return count


def check_valid_position(i, i2, j, j2, mapp):
    if i + i2 < len(mapp) and i + i2 >= 0 and j + j2 < len(mapp[0]) and j + j2 >= 0:
        return True
    return False


def get_antennas_dict(file_content: str, mapp: list) -> dict:
    antennas = set(file_content)
    antennas.remove("\n")
    antennas.remove(".")
    antennas_dict = {}
    for v in antennas:
        antennas_dict[v] = {}

    for i, line in enumerate(mapp):
        for j, c in enumerate(line):
            if c in antennas_dict:
                antennas_dict[c][(i, j)] = []

    return antennas_dict


def calculate_distances(antennas_dict: dict) -> dict:
    for antenna, positions in antennas_dict.items():
        for pos in positions:
            for pos2 in positions:
                if pos != pos2:
                    antennas_dict[antenna][(pos)].append(calculate_distance(pos, pos2))

    return antennas_dict


def calculate_distance(pos1, pos2):
    return pos1[0] - pos2[0], pos1[1] - pos2[1]


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def display_map(mapp):
    for line in mapp:
        print("".join(line))


if __name__ == "__main__":
    main()
