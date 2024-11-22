def main():
    file_content = read_file("puzzle_input.txt")

    city_dict = get_city_dict(file_content)

    results = []
    get_city_combinations(city_dict.keys(), [], results)
    low_distance = get_low_distance(results, city_dict)
    print(low_distance)


def get_city_dict(file_content: list) -> dict:
    city_dict = {}
    for s in file_content:
        aux = s.split()
        if aux[0] not in city_dict:
            city_dict[aux[0]] = {}
        if aux[2] not in city_dict:
            city_dict[aux[2]] = {}

        city_dict[aux[0]][aux[2]] = aux[-1]
        city_dict[aux[2]][aux[0]] = aux[-1]
    return city_dict


def get_city_combinations(cities: list, current_comb: list, results: list) -> list:
    if len(current_comb) == len(cities):
        results.append(current_comb.copy())
        return

    for city in cities:
        if city not in current_comb:
            current_comb.append(city)
            get_city_combinations(cities, current_comb, results)
            current_comb.pop()


def get_low_distance(cities_comb: list, cities_dict: dict) -> int:
    results = []
    for c_comb in cities_comb:
        partial_result = 0
        for i in range(0, len(c_comb) - 1):
            partial_result += int(cities_dict[c_comb[i]][c_comb[i + 1]])
        results.append(partial_result)

    results.sort()
    return results[0]


def read_file(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
