import re


def main():
    file_content = read_file("example.txt")

    # pt 1
    nums = get_multiplications(file_content)
    print(get_result(nums))


def get_result(nums: list) -> int:
    result = 0
    for num in nums:
        result += int(num[0]) * int(num[1])
    return result


def get_multiplications(file_content: str) -> list:
    patron = re.compile(r"mul\((\d+),(\d+)\)")
    matches = patron.findall(file_content)
    return matches


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
