def main():
    file_content = read_file("mini_example.txt")
    garden = get_garden(file_content)
    coords = set()
    plots = {}
    plot_id = 0
    for i, row in enumerate(garden):
        for j, item in enumerate(row):
            if (i, j) not in coords:
                get_same_plots(garden, i, j, coords, plots, plot_id)
                plot_id += 1

    print(plots)


def get_same_plots(
    garden: list, i: int, j: int, coords: set, plots: dict, plot_id: int
):
    if (i, j) in coords:
        return
    if plot_id not in plots:
        plots[plot_id] = {"area": 0, "sides": 4}

    coords.add((i, j))
    plots[plot_id]["area"] += 1

    val = garden[i][j]
    if i > 0 and val == garden[i - 1][j]:
        get_same_plots(garden, i - 1, j, coords, plots, plot_id)

    if i < len(garden) - 1 and val == garden[i + 1][j]:
        get_same_plots(garden, i + 1, j, coords, plots, plot_id)

    if j > 0 and val == garden[i][j - 1]:
        get_same_plots(garden, i, j - 1, coords, plots, plot_id)

    if j < len(garden[i]) - 1 and val == garden[i][j + 1]:
        get_same_plots(garden, i, j + 1, coords, plots, plot_id)


def read_file(filename):
    with open(filename) as f:
        return f.read()


def get_garden(file_content):
    rows = file_content.split("\n")
    garden = []
    for row in rows:
        garden.append(list(row))
    return garden


if __name__ == "__main__":
    main()
