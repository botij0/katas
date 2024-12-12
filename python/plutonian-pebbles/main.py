def main():
    file_content = read_file("puzzle_input.txt")
    stones = [int(x) for x in file_content.split()]
    for i in range(75):
        stones = proccess_stones_iteration(stones)
    print(len(stones))


def proccess_stones_iteration(stones: list) -> list:
    aux = []
    for stone in stones:
        if stone == 0:
            aux.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            aux.append(int(stone_str[0 : int(len(stone_str) / 2)]))
            aux.append(int(stone_str[int(len(stone_str) / 2) :]))
        else:
            aux.append(stone * 2024)

    return aux


def read_file(filename: str):
    with open(filename) as f:
        return f.read()


if __name__ == "__main__":
    main()
