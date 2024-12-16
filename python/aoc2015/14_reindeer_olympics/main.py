def main():
    reindeers = get_reindeer_dict(read_file("puzzle_input.txt"))
    process_reindeers_pt2(reindeers, 2503)


def process_reindeers_pt2(reindeers: dict, max_seconds: int):
    for sec in range(1, max_seconds + 1):
        for key in reindeers.keys():
            if (
                reindeers[key]["partial_count"]
                >= reindeers[key]["time"] + reindeers[key]["cooldown"]
            ):
                reindeers[key]["partial_count"] = 0

            if not (
                reindeers[key]["partial_count"] >= reindeers[key]["time"]
                and reindeers[key]["partial_count"]
                < (reindeers[key]["time"] + reindeers[key]["cooldown"])
            ):
                reindeers[key]["distance"] += reindeers[key]["speed"]

            reindeers[key]["partial_count"] += 1
        give_point(reindeers)

    for key in reindeers:
        print(f"{key} - {reindeers[key]["point"]}")


def give_point(reindeers: dict):
    winners = get_winner(reindeers)
    for winner in winners:
        reindeers[winner]["point"] += 1


def get_winner(reindeers: dict) -> list:
    distances = sorted([reindeers[key]["distance"] for key in reindeers])
    max_distance = distances[-1]
    winners = []
    for key in reindeers.keys():
        if reindeers[key]["distance"] == max_distance:
            winners.append(key)

    return winners


def proccess_reindeers_pt1(reindeers: dict, max_seconds: int):
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
            "partial_count": 0,
            "point": 0,
        }
    return reindeers


def read_file(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
