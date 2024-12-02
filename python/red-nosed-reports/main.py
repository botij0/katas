def main():
    file_content = read_file("puzzle_input.txt")
    print(get_reports_safe(file_content))


def get_reports_safe(reports: list) -> int:
    count = 0
    for report in reports:
        aux = [int(n) for n in report.split(" ")]
        aux_count = check_report(aux.copy())
        if aux_count == 0:
            aux_count = check_report_2(aux.copy())
        count += aux_count
    return count


def check_report(report: list, changes: int = 0):
    if changes > 1:
        return 0
    ascending = report[0] < report[1]

    for i in range(0, len(report) - 1):
        if report[i] == report[i + 1]:
            report.pop(i)
            return 0 if check_report(report, changes + 1) == 0 else 1

        if not check_correct_levels(report[i], report[i + 1], ascending):
            report.pop(i)
            return 0 if check_report(report, changes + 1) == 0 else 1
        else:
            if not check_diff(report[i], report[i + 1], ascending):
                report.pop(i + 1)
                return 0 if check_report(report, changes + 1) == 0 else 1
    return 1


def check_report_2(report: list, changes: int = 0):
    if changes > 1:
        return 0
    ascending = report[0] < report[1]

    for i in range(0, len(report) - 1):
        if report[i] == report[i + 1]:
            report.pop(i + 1)
            return 0 if check_report(report, changes + 1) == 0 else 1

        if not check_correct_levels(report[i], report[i + 1], ascending):
            report.pop(i + 1)
            return 0 if check_report(report, changes + 1) == 0 else 1
        else:
            if not check_diff(report[i], report[i + 1], ascending):
                report.pop(i)
                return 0 if check_report(report, changes + 1) == 0 else 1
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
