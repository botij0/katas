def main():
    file_content = read_file("mini_example.txt")
    file_content = replace_free_space(file_content)
    print(file_content)
    file_blocks = move_file_blocks(file_content)
    print(file_blocks)
    checksum = get_checksum(file_blocks)
    print(checksum)


def get_checksum(file_blocks: str) -> int:
    blocks = list(file_blocks)
    total = 0
    for i in range(len(blocks)):
        total += int(blocks[i]) * i
        if total >= 9223372036854775:
            print("Overflow")
    return total


def move_file_blocks(file_content: str) -> str:
    if file_content.find(".") == -1:
        return file_content
    content_list = list(file_content)
    i = len(content_list) - 1
    while i >= 0:
        if content_list[i] != ".":
            index = content_list.index(".")
            if index > i:
                break
            content_list[index] = content_list[i]
            content_list[i] = "."
        i -= 1
    return "".join(content_list).replace(".", "")


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
