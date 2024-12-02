def main():
    file_content = read_file("puzzle_input.txt")
    print(get_reports_safe(file_content))


def get_reports_safe(reports: list) -> int:
    count = 0
    for report in reports:
        count += check_report(report)

    return count


def check_report(report: str):
    aux = [int(n) for n in report.split(" ")]
    ascending = aux[0] < aux[1]

    for i in range(0, len(aux) - 1):
        if aux[i] == aux[i + 1]:
            return 0

        if not check_correct_levels(aux[i], aux[i + 1], ascending):
            return 0
        else:
            if not check_diff(aux[i], aux[i + 1], ascending):
                return 0
    return 1


def check_correct_levels(a: int, b: int, ascending: bool) -> bool:
    if ascending is True and a > b:
        return False
    if ascending is False and b > a:
        return False
    return True


def check_diff(a: int, b: int, ascending: bool) -> bool:
    if ascending is True and b - a > 3:
        return False
    elif ascending is False and a - b > 3:
        return False
    return True


def read_file(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
