import json

EXAMPLE_RESULT = 18


def main():
    file = read_json("puzzle_input.json")
    process_puzzle(file)


def process_puzzle(file):
    total = 0
    for val in file:
        if isinstance(val, list):
            total += process_list(val)
        elif isinstance(val, dict):
            total += process_dict(val)

    print(total)


def process_list(x_list: list) -> int:
    total = 0
    for value in x_list:
        if isinstance(value, int):
            total += value

        elif isinstance(value, list):
            total += process_list(value)

        elif isinstance(value, dict):
            total += process_dict(value)
    return total


def process_dict(x_dict: dict) -> int:
    total = 0
    if "red" not in x_dict.keys() and "red" not in x_dict.values():
        for value in x_dict.values():
            if isinstance(value, int):
                total += value
            elif isinstance(value, list):
                total += process_list(value)
            elif isinstance(value, dict):
                total += process_dict(value)

    return total


def read_json(filename: str) -> list:
    with open(filename, "r") as f:
        return json.load(f)


if __name__ == "__main__":
    main()
