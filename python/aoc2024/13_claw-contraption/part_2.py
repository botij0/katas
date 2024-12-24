def main():
    file_contents = read_file("puzzle_input.txt")
    buttons_dict = get_buttons_list(file_contents)
    total = 0
    for btn in buttons_dict:
        x, y = get_result(
            btn["a"]["x"],
            btn["a"]["y"],
            btn["b"]["x"],
            btn["b"]["y"],
            btn["p"]["x"],
            btn["p"]["y"],
        )
        if check_valid_result(x, y):
            total += (3 * x) + y

    print(total)


def check_valid_result(x: int, y: int) -> bool:
    if len(str(x).split(".")[-1]) == 1 and len(str(y).split(".")[-1]) == 1:
        return True
    return False


# Sistema de ecuaciones
def get_result(ax: int, ay: int, bx: int, by: int, px: int, py: int) -> tuple[int, int]:
    y = ((ax * py) - (ay * px)) / ((by * ax) - (bx * ay))
    x = (px - bx * y) / ax
    return x, y


def get_buttons_list(file_contents: list) -> list[dict]:
    buttons_list = []
    for _, file_content in enumerate(file_contents):
        buttons = file_content.split("\n")
        buttons_dict = {
            "a": {"x": 0, "y": 0},
            "b": {"x": 0, "y": 0},
            "p": {"x": 0, "y": 0},
        }
        for button in buttons:
            aux = button.split(":")[1].strip().split(",")
            if button.startswith("Button A:"):
                buttons_dict["a"]["x"] = int(aux[0].split("X+")[-1])
                buttons_dict["a"]["y"] = int(aux[1].split("Y+")[-1])
            elif button.startswith("Button B:"):
                buttons_dict["b"]["x"] = int(aux[0].split("X+")[-1])
                buttons_dict["b"]["y"] = int(aux[1].split("Y+")[-1])
            elif button.startswith("Prize:"):
                buttons_dict["p"]["x"] = int(aux[0].split("X=")[-1]) + 10000000000000
                buttons_dict["p"]["y"] = int(aux[1].split("Y=")[-1]) + 10000000000000
        buttons_list.append(buttons_dict)

    return buttons_list


def read_file(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    main()
