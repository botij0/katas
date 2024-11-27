def main():
    reindeers = get_reindeer_dict(read_file("puzzle_input.txt"))
    proccess_reindeers(reindeers, 2503)


def proccess_reindeers(reindeers: dict, max_seconds: int):
    for key in reindeers.keys():
        partial_time = reindeers[key]["time"] + reindeers[key]["cooldown"]
        cicles = int(max_seconds / partial_time)
        left_seconds = max_seconds % partial_time
        reindeers[key]["distance"] += (
            reindeers[key]["time"] * reindeers[key]["speed"] * cicles
        )
        if reindeers[key]["time"] <= left_seconds:
            reindeers[key]["distance"] += (
                reindeers[key]["time"] * reindeers[key]["speed"]
            )
        else:
            reindeers[key]["distance"] += left_seconds * reindeers[key]["speed"]

        print(f"{key} - {reindeers[key]["distance"]} km")


def get_reindeer_dict(content: list) -> dict:
    reindeers = {}
    for row in content:
        aux = row.split(" ")
        reindeers[aux[0]] = {
            "speed": int(aux[3]),
            "time": int(aux[6]),
            "cooldown": int(aux[-2]),
            "distance": 0,
        }
    return reindeers


def read_file(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
