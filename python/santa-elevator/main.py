def main():
    file_content = read_file("puzzle_input.txt")
    print(get_first_basement(file_content))


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def get_final_floor(file_content: str) -> int:
    up_count = file_content.count("(")
    down_count = file_content.count(")")
    return up_count - down_count


def get_first_basement(file_content: str) -> int:
    current_floor = 0
    for i, char in enumerate(file_content):
        if char == "(":
            current_floor += 1
        elif char == ")":
            current_floor -= 1

        if current_floor == -1:
            return i + 1


if __name__ == "__main__":
    main()
