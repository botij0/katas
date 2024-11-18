MAP = [[0] * 1000 for _ in range(1000)]


def main():
    file_content = read_file("puzzle_input.txt")
    instruct_list = file_content.split("\n")
    for ins in instruct_list:
        process_operation(get_operation(ins))

    lights_on = 0
    for row in MAP:
        lights_on += row.count(1)
    print(lights_on)


def get_operation(s: str) -> dict:
    inst_list = s.split(" ")
    if len(inst_list) == 5:
        return {
            "operation": inst_list[0] + " " + inst_list[1],
            "from_coordinates": format_coordinates(inst_list[2]),
            "to_coordinates": format_coordinates(inst_list[4]),
        }
    else:
        return {
            "operation": inst_list[0],
            "from_coordinates": format_coordinates(inst_list[1]),
            "to_coordinates": format_coordinates(inst_list[3]),
        }


def process_operation(op_dict: dict):
    op = op_dict["operation"]
    from_coords = op_dict["from_coordinates"]
    to_coords = op_dict["to_coordinates"]

    for i in range(from_coords[1], to_coords[1] + 1):
        for j in range(from_coords[0], to_coords[0] + 1):
            if op == "turn off":
                turn_off_light(i, j)
            elif op == "turn on":
                turn_on_light(i, j)
            else:
                toggle_light(i, j)


def format_coordinates(coord: str) -> list:
    coord_list = coord.split(",")
    coor_list_int = [int(n) for n in coord_list]
    return coor_list_int


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
