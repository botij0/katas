from itertools import permutations

OPERATOR = {"gain": 1, "lose": -1}


def main():
    people = get_people_dict(read_file("puzzle_input.txt"))
    print(get_happiness(get_permutations(people), people))


def read_file(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().split("\n")


def get_people_dict(content: list) -> dict:
    people = {}
    for row in content:
        aux = row[:-1].split(" ")
        if aux[0] not in people:
            people[aux[0]] = {}

        people[aux[0]][aux[-1]] = int(aux[3]) * OPERATOR[aux[2]]

    return people


def get_permutations(people: dict) -> list:
    return list(permutations(people.keys()))


def get_happiness(permutations: list, people: dict) -> int:
    max_happiness = 0
    for perm in permutations:
        partial_happiness = 0

        # Center Cases
        for i in range(1, len(perm) - 1):
            partial_happiness += people[perm[i]][perm[i + 1]]
            partial_happiness += people[perm[i]][perm[i - 1]]

        # Edges Cases
        partial_happiness += people[perm[0]][perm[1]]
        partial_happiness += people[perm[0]][perm[-1]]
        partial_happiness += people[perm[-1]][perm[0]]
        partial_happiness += people[perm[-1]][perm[-2]]

        if max_happiness < partial_happiness:
            max_happiness = partial_happiness

    return max_happiness


if __name__ == "__main__":
    main()
