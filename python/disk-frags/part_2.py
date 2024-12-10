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
    free_space_dict = get_free_space_dict(mapp)
    print(free_space_dict)
    for i in range(len(mapp) - 1, -1, -1):
        if mapp[i] != ".":
            file_block = get_file_block_count(mapp, i)
            for k, v in free_space_dict.items():
                if v >= file_block and i > k:
                    mapp[k : k + file_block] = mapp[i - file_block + 1 : i + 1]
                    mapp[i - file_block + 1 : i + 1] = ["."] * file_block
                    free_space_dict = get_free_space_dict(mapp)
                    break

    return mapp


def get_free_space_dict(mapp: list) -> dict:
    free_space_dict = {}
    i = 0
    while i < len(mapp):
        if mapp[i] == ".":
            free_space_count = get_free_space(mapp, i)
            free_space_dict[i] = free_space_count
            i += free_space_count
        else:
            i += 1
    return free_space_dict


def get_file_block_count(mapp: list, index: int) -> str:
    return mapp.count(mapp[index])


def get_free_space(mapp: list, index: int) -> int:
    if index >= len(mapp):
        return 0
    free_space = 0

    while index < len(mapp) and mapp[index] == ".":
        free_space += 1
        index += 1
    return free_space


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
