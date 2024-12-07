operator_dict = {"+": lambda x, y: x + y, "*": lambda x, y: x * y}


def main():
    file_contents = read_file("puzzle_input.txt")
    bridge_dict = get_bridge_dict(file_contents)
    total = 0
    for bridge_id, bridge in bridge_dict.items():
        combs = []
        get_operators_combs(len(bridge) - 1, [], combs)
        if check_bridge(bridge_id, bridge, combs):
            total += bridge_id
    print(f"total repaired: {total}")


def check_bridge(bridge_id: int, bridge: list, combination: list):
    for comb in combination:
        x = bridge[0]
        for i in range(len(comb)):
            x = operator_dict[comb[i]](x, bridge[i + 1])
            if x > bridge_id:
                break
        if x == bridge_id:
            return True
    return False


def get_bridge_dict(file_contents):
    bridge_dict = {}
    for line in file_contents:
        bridge_id, bridge = line.split(":")
        bridge_dict[int(bridge_id)] = [int(x) for x in bridge.split()]
    return bridge_dict


def get_operators_combs(spaces: int, current_combination: list, results: list):
    simbolos = ["+", "*"]
    if len(current_combination) == spaces:
        results.append(current_combination)
        return

    for simbolo in simbolos:
        get_operators_combs(spaces, current_combination + [simbolo], results)


def read_file(filename):
    with open(filename) as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
