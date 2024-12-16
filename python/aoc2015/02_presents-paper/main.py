from typing import List


def main():
    orders = read_file("puzzle_input.txt")
    orders_list = orders.split("\n")
    print(process_orders(orders_list))


def process_orders(orders_list: List[str]) -> int:
    total_orders = 0
    total_ribbon = 0
    for order in orders_list:
        total_orders += get_total_order(order)
        total_ribbon += get_total_ribbon(order)
    return total_orders, total_ribbon


def get_total_ribbon(order: str) -> int:
    metrics = order.split("x")
    metrics = [int(n) for n in metrics]
    metrics.sort()
    return get_perimeter(metrics[0], metrics[1]) + get_bow_made(metrics)


def get_bow_made(metrics: List[int]) -> int:
    total = 1
    for metric in metrics:
        total *= metric
    return total


def get_perimeter(a: int, b: int) -> int:
    return (a * 2) + (b * 2)


def get_total_order(order: str) -> int:
    metrics = order.split("x")
    areas = get_areas(metrics)
    total = 0
    for area in areas:
        total += 2 * area
    return total + areas[0]


def get_areas(metrics_list: List[str]) -> List[int]:
    if len(metrics_list) != 3:
        raise "ERROR, the present must be a box with 3 metrics"

    metrics = [int(n) for n in metrics_list]
    areas = [metrics[0] * metrics[1], metrics[0] * metrics[2], metrics[1] * metrics[2]]
    areas.sort()
    return areas


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
