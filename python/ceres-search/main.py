def main():
    file_content = read_file("example.txt")
    total = (
        get_inverse_horizontal_xmas(file_content)  # si 3
        + get_horizontal_xmas(file_content)  # si 2
        + get_vertical_xmas(file_content)  # si 1
        + get_inverse_vertical_xmas(file_content)  # si 2
        + get_diagonal_xmas(file_content)  # no 8
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
                    count += check_down_diagonal(rows_map, i, j)
            elif i >= len(rows_map) - 3:
                if rows_map[i][j] == "X":
                    count += check_up_diagonal(rows_map, i, j)
            else:
                if rows_map[i][j] == "X":
                    count += check_down_diagonal(rows_map, i, j)
                    count += check_up_diagonal(rows_map, i, j)
    return count


def check_down_diagonal(r: list[list[str]], i: int, j: int) -> int:
    if j < 3:
        return (
            1
            if r[i + 1][j + 1] == "M"
            and r[i + 2][j + 2] == "A"
            and r[i + 3][j + 3] == "S"
            else 0
        )
    elif j >= len(r[i]) - 3:
        return (
            1
            if r[i + 1][j - 1] == "M"
            and r[i + 2][j - 2] == "A"
            and r[i + 3][j - 3] == "S"
            else 0
        )
    else:
        return (
            1
            if (
                r[i + 1][j + 1] == "M"
                and r[i + 2][j + 2] == "A"
                and r[i + 3][j + 3] == "S"
            )
            or (
                r[i + 1][j - 1] == "M"
                and r[i + 2][j - 2] == "A"
                and r[i + 3][j - 3] == "S"
            )
            else 0
        )


def check_up_diagonal(r: list[list[str]], i: int, j: int) -> int:
    if j < 3:
        return (
            1
            if r[i - 1][j + 1] == "M"
            and r[i - 2][j + 2] == "A"
            and r[i - 3][j + 3] == "S"
            else 0
        )
    elif j >= len(r[i]) - 3:
        return (
            1
            if r[i - 1][j - 1] == "M"
            and r[i - 2][j - 2] == "A"
            and r[i - 3][j - 3] == "S"
            else 0
        )
    else:
        return (
            1
            if (
                r[i - 1][j + 1] == "M"
                and r[i - 2][j + 2] == "A"
                and r[i - 3][j + 3] == "S"
            )
            or (
                r[i - 1][j - 1] == "M"
                and r[i - 2][j - 2] == "A"
                and r[i - 3][j - 3] == "S"
            )
            else 0
        )


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
