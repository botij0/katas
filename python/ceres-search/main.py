def main():
    file_content = read_file("puzzle_input.txt")
    total = (
        get_inverse_horizontal_xmas(file_content)
        + get_horizontal_xmas(file_content)
        + get_vertical_xmas(file_content)
        + get_inverse_vertical_xmas(file_content)
        + get_diagonal_xmas(file_content)
    )
    print(get_diagonal_xmas(file_content))
    print(total)


def get_diagonal_xmas(file_content: str) -> int:
    rows_map = [list(s) for s in file_content.split()]
    count = 0
    for i in range(len(rows_map)):
        for j in range(len(rows_map[i])):
            if i < 3:
                if rows_map[i][j] == "X":
                    count += check_diagonal(rows_map, i, j, "down")
            elif i >= len(rows_map) - 3:
                if rows_map[i][j] == "X":
                    count += check_diagonal(rows_map, i, j, "up")
            else:
                if rows_map[i][j] == "X":
                    count += check_diagonal(rows_map, i, j, "down")
                    count += check_diagonal(rows_map, i, j, "up")
    return count


def check_diagonal(r: list[list[str]], i: int, j: int, orientation: str) -> int:
    sign = 1 if orientation == "down" else -1
    if j < 3:
        return (
            1
            if r[i + sign * 1][j + 1] == "M"
            and r[i + sign * 2][j + 2] == "A"
            and r[i + sign * 3][j + 3] == "S"
            else 0
        )
    elif j >= len(r[i]) - 3:
        return (
            1
            if r[i + sign * 1][j - 1] == "M"
            and r[i + sign * 2][j - 2] == "A"
            and r[i + sign * 3][j - 3] == "S"
            else 0
        )
    else:
        aux = 0
        aux += (
            1
            if (
                r[i + sign * 1][j + 1] == "M"
                and r[i + sign * 2][j + 2] == "A"
                and r[i + sign * 3][j + 3] == "S"
            )
            else 0
        )
        aux += (
            1
            if (
                r[i + sign * 1][j - 1] == "M"
                and r[i + sign * 2][j - 2] == "A"
                and r[i + sign * 3][j - 3] == "S"
            )
            else 0
        )
        return aux


def get_horizontal_xmas(file_content: str) -> int:
    return file_content.count("XMAS")


def get_inverse_horizontal_xmas(file_content: str) -> int:
    return file_content.count("SAMX")


def get_vertical_xmas(file_content: str) -> int:
    rows_map = [list(s) for s in file_content.split()]
    rows_trasposed = get_trasposed_matrix(rows_map)
    content_trasposed = matrix_to_string(rows_trasposed)
    return content_trasposed.count("XMAS")


def get_inverse_vertical_xmas(file_content: str) -> int:
    rows_map = [list(s) for s in file_content.split()]
    rows_trasposed = get_trasposed_matrix(rows_map)
    content_trasposed = matrix_to_string(rows_trasposed)
    return content_trasposed.count("SAMX")


def get_trasposed_matrix(matrix: list[list[str]]) -> list[list[str]]:
    return list(map(list, zip(*matrix)))


def matrix_to_string(matrix: list[list[str]]) -> str:
    return "\n".join(map(lambda row: "".join(row), matrix))


def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


if __name__ == "__main__":
    main()
