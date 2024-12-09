def main():
    file_content = read_file("puzzle_input.txt")
    mapp = replace_free_space(file_content)
    print(mapp)
    file_blocks = move_file_blocks(mapp)
    print(file_blocks)
    checksum = get_checksum(file_blocks)
    print(checksum)


def get_checksum(file_blocks: str) -> int:
    blocks = list(file_blocks)
    total = 0
    for i in range(len(blocks)):
        if blocks[i] != ".":
            total += int(blocks[i]) * i
    return total


def move_file_blocks(mapp: list) -> list:
    try:
        mapp.index(".")
    except ValueError:
        return mapp

    i = len(mapp) - 1
    while i >= 0:
        if mapp[i] != ".":
            index = mapp.index(".")
            if index > i:
                break
            mapp[index] = mapp[i]
            mapp[i] = "."
        i -= 1
    return mapp


def replace_free_space(file_content: str) -> list:
    mapp = []
    files_count = 0
    for i in range(len(file_content)):
        x = int(file_content[i])
        if i % 2 != 0:
            for _ in range(x):
                mapp.append(".")
        else:
            for _ in range(x):
                mapp.append(str(files_count))
            files_count += 1

    return mapp


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
