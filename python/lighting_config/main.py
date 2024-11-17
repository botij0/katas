from enum import Enum


MAP = [[0] * 1000 for _ in range(1000)]


def main():
    file_content = read_file("puzzle_input.txt")
    instruct_list = file_content.split("\n")
    get_operation(instruct_list[0])


def get_operation(s: str) -> dict:
    inst_list = s.split(" ")
    if len(inst_list) == 5:
        return {
            "operation": inst_list[0] + " " + inst_list[1],
            "from_coordinates": inst_list[2],
            "to_coordinates": inst_list[4],
        }
    else:
        return {
            "operation": inst_list[0],
            "from_coordinates": inst_list[1],
            "to_coordinates": inst_list[3],
        }


# Three Operations: turn off, turn on, toggle.


def turn_on_light(row: int, col: int):
    MAP[row][col] = 1


def turn_off_light(row: int, col: int):
    MAP[row][col] = 0


def toggle_light(row: int, col: int):
    MAP[row][col] = 1 if MAP[row][col] == 0 else 0


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
