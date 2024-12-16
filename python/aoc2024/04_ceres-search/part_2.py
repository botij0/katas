def main():
    file_content = read_file("puzzle_input.txt")
    total = 0
    for row in range(1, len(file_content) - 1):
        for col in range(1, len(file_content[0]) - 1):
            if file_content[row][col] == "A":
                total += check_x(file_content, row, col)

    print(total)


def check_x(file_content: list, row: int, col: int) -> int:
    diagonal_1 = file_content[row - 1][col - 1] + "A" + file_content[row + 1][col + 1]
    diagonal_2 = file_content[row - 1][col + 1] + "A" + file_content[row + 1][col - 1]
    return 1 if diagonal_1 in ("SAM", "MAS") and diagonal_2 in ("SAM", "MAS") else 0


def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
