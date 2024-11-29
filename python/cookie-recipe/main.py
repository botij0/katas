MAX = 100


def main():
    ingredients = read_file("puzzle_input.txt")
    ingredients_dict = get_ingredients_dict(ingredients)
    print(ingredients_dict)
    get_better_cuantity(ingredients_dict)


def get_better_cuantity(ingredients_dict: dict):
    max_score = 0
    best_comb = None
    for x in range(1, 101):
        for y in range(1, 101 - x):
            for z in range(1, 101 - x - y):
                q = 100 - x - y - z
                score = calculate_ingredients_score(ingredients_dict, [x, y, z, q])

                if score > max_score:
                    max_score = score
                    best_comb = [x, y, z, q]

    print(best_comb)
    print(max_score)


def calculate_ingredients_score(ingredients_dict: dict, comb: list[int]) -> int:
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for i, key in enumerate(ingredients_dict.keys()):
        capacity += ingredients_dict[key]["capacity"] * comb[i]
        durability += ingredients_dict[key]["durability"] * comb[i]
        flavor += ingredients_dict[key]["flavor"] * comb[i]
        texture += ingredients_dict[key]["texture"] * comb[i]

    return get_score(capacity, durability, flavor, texture)


def get_ingredients_dict(ingredients: list) -> dict:
    ingredients_dict = {}
    for ingredient in ingredients:
        name, values = ingredient.split(":")
        values = values.split(",")
        ingredients_dict[name] = {
            "capacity": int(values[0].split(" ")[-1]),
            "durability": int(values[1].split(" ")[-1]),
            "flavor": int(values[2].split(" ")[-1]),
            "texture": int(values[3].split(" ")[-1]),
            "calories": int(values[4].split(" ")[-1]),
        }

    return ingredients_dict


def get_score(capacity: int, durability: int, flavor: int, texture: int) -> int:
    if capacity <= 0 or durability <= 0 or flavor <= 0 or texture <= 0:
        return 0
    return capacity * durability * flavor * texture


def read_file(filename: str) -> list:
    with open(filename) as f:
        return f.readlines()


if __name__ == "__main__":
    main()
