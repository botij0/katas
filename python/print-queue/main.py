def main():
    file_content = read_file("example.txt")
    rules, updates = get_info_from_file(file_content)
    rules_dict = get_rules_dict(rules)
    print(process_updates(updates, rules_dict))


def process_updates(updates: list, rules_dict: dict) -> int:
    is_valid = True
    count = 0
    for update in updates:
        update = update.split(",")
        for i in range(1, len(update)):
            print(update, i)
            if update[i] not in rules_dict:
                continue
            else:
                for j in range(0, i):
                    if update[j] in rules_dict[update[i]]:
                        print(update, update[j], rules_dict[update[i]], update[i])
                        is_valid = False
                        break
        if is_valid:
            print(update)
            count += int(update[int(len(update) / 2)])
    return count


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
