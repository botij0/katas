def main():
    file_contents = read_file("puzzle_input.txt")
    robots = get_robots_list(file_contents)
    final_positions = [get_final_position_robot(robot) for robot in robots]
    safety_factor = get_safety_factor(final_positions)
    print(safety_factor)


def get_middles(x: int, y: int) -> tuple[int, int]:
    return x // 2, y // 2


def get_safety_factor(final_positions: list[tuple]) -> int:
    cuadrants = [0, 0, 0, 0]
    x, y = get_middles(101, 103)
    for pos in final_positions:
        if pos[0] == x or pos[1] == y:
            continue
        if pos[0] < x and pos[1] < y:
            cuadrants[0] += 1
        elif pos[0] < x and pos[1] > y:
            cuadrants[1] += 1
        elif pos[0] > x and pos[1] < y:
            cuadrants[2] += 1
        elif pos[0] > x and pos[1] > y:
            cuadrants[3] += 1

    return cuadrants[0] * cuadrants[1] * cuadrants[2] * cuadrants[3]


def get_robots_list(file_contents: list[str]) -> list[dict]:
    robots = []
    for line in file_contents:
        p, v = line.split(" ")
        robot = {"p": (0, 0), "v": (0, 0)}
        robot["p"] = (
            int(p.split("=")[-1].split(",")[0]),
            int(p.split("=")[-1].split(",")[1]),
        )
        robot["v"] = (
            int(v.split("=")[-1].split(",")[0]),
            int(v.split("=")[-1].split(",")[1]),
        )
        robots.append(robot)
    return robots


def get_final_position_robot(robot: dict) -> tuple:
    pos = robot["p"]
    for i in range(100):
        pos = move_robot(pos, robot["v"])

    return pos


def move_robot(pos: tuple, v: tuple) -> tuple:
    pos1 = pos[0] + v[0]
    pos2 = pos[1] + v[1]
    if pos1 < 0:
        pos1 += 101
    elif pos1 >= 101:
        pos1 -= 101
    if pos2 < 0:
        pos2 += 103
    elif pos2 >= 103:
        pos2 -= 103
    pos = (pos1, pos2)
    return pos


def read_file(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
