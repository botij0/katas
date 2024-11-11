from utils.common import is_center, logger, exec_time, is_corner
from constant.data import emojis, SOLUTION


@exec_time
def check_array(array: list[str], len_x: int, len_y: int):
    my_sol = array.copy()
    logger.info("Calculando Mapa...")
    for i in range(0, len_x):
        for j in range(0, len_y):
            if array[i][j] == emojis["calabaza"]:
                if is_corner(i, j, len_x, len_y):
                    values_ads, values_dig = check_corners(i, j, array, len_x, len_y)
                elif is_center(i, j, len_x, len_y):
                    values_ads, values_dig = check_center(i, j, array)
                else:
                    values_ads, values_dig = check_aristas(i, j, array, len_x, len_y)
                my_sol[i][j] = get_value(my_sol[i][j], values_ads, values_dig)
        #     print(my_sol[i][j], end=" ")
        # print()
    logger.info("Array Correcto? - " + str(my_sol == SOLUTION))


def check_center(i: int, j: int, array: list[str]):
    values_ads = [
        array[i][j + 1],
        array[i][j - 1],
        array[i + 1][j],
        array[i - 1][j],
    ]
    values_dig = [
        array[i + 1][j + 1],
        array[i + 1][j - 1],
        array[i - 1][j + 1],
        array[i - 1][j - 1],
    ]
    return values_ads, values_dig


def check_corners(i: int, j: int, array: list[str], len_x: int, len_y: int):
    values_ads, values_dig = ([], [])
    if i == 0 and j == 0:
        values_ads = [array[i][j + 1], array[i + 1][j]]
        values_dig = [array[i + 1][j + 1]]

    elif i == 0 and j == len_y - 1:
        values_ads = [array[i][j - 1], array[i + 1][j]]
        values_dig = [array[i + 1][j - 1]]

    elif i == len_x - 1 and j == 0:
        values_ads = [array[i - 1][j], array[i][j + 1]]
        values_dig = [array[i - 1][j + 1]]

    elif i == len_x - 1 and j == len_y - 1:
        values_ads = [array[i - 1][j], array[i][j - 1]]
        values_dig = [array[i - 1][j - 1]]

    return values_ads, values_dig


def check_aristas(i: int, j: int, array: list[str], len_x: int, len_y: int):
    values_ads, values_dig = ([], [])
    if i == 0 and (j != 0 and j != len_y - 1):
        values_ads = [array[i][j + 1], array[i][j - 1], array[i + 1][j]]
        values_dig = [array[i + 1][j + 1], array[i + 1][j - 1]]

    elif i == len_x - 1 and (j != 0 and j != len_y - 1):
        values_ads = [array[i][j + 1], array[i][j - 1], array[i - 1][j]]
        values_dig = [array[i - 1][j + 1], array[i - 1][j - 1]]

    elif (i != 0 and i != len_x - 1) and j == 0:
        values_ads = [array[i - 1][j], array[i + 1][j], array[i][j + 1]]
        values_dig = [array[i - 1][j + 1], array[i + 1][j + 1]]

    elif (i != 0 and i != len_x - 1) and j == len_y - 1:
        values_ads = [array[i - 1][j], array[i + 1][j], array[i][j - 1]]
        values_dig = [array[i - 1][j - 1], array[i + 1][j - 1]]

    return values_ads, values_dig


def get_value(current_value: str, v_ads: list[str], v_dig: list[str]):
    if emojis["sello"] in v_ads:
        return emojis["calavera"]
    elif emojis["caramelo"] in v_ads:
        return emojis["arcoiris"]
    elif emojis["reliquia"] in v_dig or emojis["reliquia"] in v_ads:
        return emojis["arcoiris"]
    else:
        return current_value


def main():
    # check_array(INITIAL, len(INITIAL), len(INITIAL[0]))
    paths = [
        "src/constant/map.txt",
        "src/constant/random_huge.txt",
        "src/constant/random_enormous.txt",
        "src/constant/random_large.txt",
    ]
    try:
        with open(paths[2], "r") as f:
            array = f.read().splitlines()
            array = [line.split() for line in array]
            check_array(array, len(array), len(array[0]))
    except FileNotFoundError:
        logger.error("No se encontró el archivo de mapa")
        exit(-1)


if __name__ == "__main__":
    main()
