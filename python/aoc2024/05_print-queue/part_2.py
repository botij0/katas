def main():
    file_content = read_file("puzzle_input.txt")
    rules, updates = get_info_from_file(file_content)
    rules_dict = get_rules_dict(rules)
    incorrect_updates = get_incorrect_updates(updates, rules_dict)

    corrected_updates = []
    total = 0
    for in_update in incorrect_updates:
        aux = correct_update(in_update, rules_dict)
        total += int(aux[int(len(aux) / 2)])
        corrected_updates.append(aux)
    print(total)


def get_incorrect_updates(updates: list, rules_dict: dict) -> list:
    incorrect_updates = []
    for update in updates:
        is_invalid = False
        update = update.split(",")
        for i in range(1, len(update)):
            if update[i] not in rules_dict:
                continue
            else:
                for j in range(0, i):
                    if update[j] in rules_dict[update[i]]:
                        is_invalid = True
                        incorrect_updates.append(update)
                        break
                if is_invalid:
                    break

    return incorrect_updates


def correct_update(update: list, rules_dict: dict) -> list:
    for i in range(1, len(update)):
        if update[i] not in rules_dict:
            continue
        for j in range(0, i):
            if update[j] in rules_dict[update[i]]:
                aux = update[j]
                update[j] = update[i]
                update[i] = aux
                update = correct_update(update, rules_dict)
                break
    return update


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def get_info_from_file(file_content: str) -> list:
    info = file_content.split("\n\n")
    return info[0].split("\n"), info[1].split("\n")


def get_rules_dict(rules: list) -> dict:
    rules_dict = {}
    for rule in rules:
        rule = rule.split("|")
        if rule[0] not in rules_dict:
            rules_dict[rule[0]] = []
        rules_dict[rule[0]].append(rule[1])
    return rules_dict


if __name__ == "__main__":
    main()
