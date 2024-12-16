def main():
    file_content = read_file("puzzle_input.txt")
    stones = [int(x) for x in file_content.split()]
    cache = {}
    total = 0
    for stone in stones:
        total += get_stones_count(stone, 75, cache)
    print(total)


def get_stones_count(stone, it: int, cache: dict) -> int:
    if it == 0:
        return 1

    if (stone, it) in cache:
        return cache[(stone, it)]

    count = 0
    new_stones = apply_rules(stone)
    for new_stone in new_stones:
        count += get_stones_count(new_stone, it - 1, cache)

    # Save the result in the cache
    cache[(stone, it)] = count
    return count


def apply_rules(stone: int) -> list:
    if stone == 0:
        return [1]

    string_stone = str(stone)
    if len(string_stone) % 2 == 0:
        left = string_stone[: len(string_stone) // 2]
        right = string_stone[len(string_stone) // 2 :]
        return [int(left), int(right)]

    return [stone * 2024]


def read_file(filename: str):
    with open(filename) as f:
        return f.read()


if __name__ == "__main__":
    main()
