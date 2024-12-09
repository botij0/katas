def main():
    file_content = read_file("example.txt")
    file_content = replace_free_space(file_content)

    file_blocks = move_file_blocks(file_content)
    print(file_blocks)
    checksum = get_checksum(file_blocks)
    print(checksum)


def get_checksum(file_content: str) -> int:
    files = list(file_content)
    total = 0
    for i in range(len(files)):
        if files[i] == ".":
            continue
        total += int(files[i]) * i
    return total


def move_file_blocks(file_content: str) -> str:
    content_list = list(file_content)
    for i in range(len(content_list) - 1, 0, -1):
        if content_list[i] == ".":
            continue
        index = content_list.index(".")
        if index == -1:
            break
        content_list[index] = content_list[i]
        content_list[i] = "."
        if content_list[:i].count(".") == 0:
            break
    return "".join(content_list)


def replace_free_space(file_content: str) -> str:
    s = ""
    files_count = 0
    for i in range(len(file_content)):
        x = int(file_content[i])
        if i % 2 != 0:
            s += "." * x
        else:
            s += str(files_count) * x
            files_count += 1

    return s


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
