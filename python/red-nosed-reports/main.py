def main():
    file_content = read_file("puzzle_input.txt")
    print(get_reports_safe_pt2(file_content))


def get_reports_safe(reports: list) -> int:
    count = 0
    for report in reports:
        aux = [int(n) for n in report.split(" ")]
        count += check_report(aux.copy())

    return count


def get_reports_safe_pt2(reports: list):
    count = 0
    for report in reports:
        aux = [int(n) for n in report.split(" ")]

        if check_report(aux) == 1:
            count += 1
        else:
            count += check_report_pt2(aux)

    return count


def check_report_pt2(report: list):
    corrects = []
    for i in range(0, len(report)):
        if corrects.count(1) >= 1:
            return 1

        x = report.copy()
        x.pop(i)
        corrects.append(check_report(x))

    return 0 if corrects.count(1) < 1 else 1


# 367
def check_report(report: list):
    ascending = report[0] < report[1]
    for i in range(0, len(report) - 1):
        if report[i] == report[i + 1]:
            return 0

        if not check_correct_levels(report[i], report[i + 1], ascending):
            return 0

        else:
            if not check_diff(report[i], report[i + 1], ascending):
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
