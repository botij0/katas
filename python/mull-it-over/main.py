import re


def main():
    file_content = read_file("example_pt2.txt")
    total_dict = (
        get_dos_dict(file_content)
        | get_dont_dict(file_content)
        | get_mults_dict(file_content)
    )
    dict_ordenado = {k: total_dict[k] for k in sorted(total_dict)}
    print(dict_ordenado)
    # pt 1
    # nums = get_multiplications(file_content)
    # print(get_result(nums))


def process_dict(dict_ordenado: dict) -> int:
    disabled = False
    total = 0
    for value in dict_ordenado.values():
        if value == "do()":
            disabled = True
        elif value == "don't()":
            disabled = False
        elif value == "mul()":
            if not disabled:
                total += 1


def get_dos_dict(file_content: str) -> dict:
    dos_dict = {}
    start = 0
    while (index := file_content.find("do()", start)) != -1:
        dos_dict[index] = "do()"
        start = index + 1
    return dos_dict


def get_dont_dict(file_content: str) -> dict:
    dont_dict = {}
    start = 0
    while (index := file_content.find("don't()", start)) != -1:
        dont_dict[index] = "don't()"
        start = index + 1
    return dont_dict


def get_mults_dict(file_content: str) -> dict:
    mult_dicts = {}
    patron = re.compile(r"mul\((\d+),(\d+)\)")
    matches = [match.start() for match in patron.finditer(file_content)]
    for match in matches:
        mult_dicts[match] = "mul()"
    return mult_dicts


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
