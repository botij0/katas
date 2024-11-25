PUZZLE_INPUT = "cqjxjnds"
EXAMPLE = "abcdefgh"
PART_2 = "cqjxxyzz"

# Ascii 97 to 122
INVALID = ["i", "l", "o"]
INVALID_NUMS = [105, 108, 111]


def main():
    print(get_new_psw(PART_2))


def get_new_psw(current_psw: str) -> str:
    aux = [ord(c) for c in list(current_psw)]
    correct_psw = False

    while correct_psw is False:
        aux[-1] += 1
        aux = update_string(aux)
        s = "".join(chr(c) for c in aux)
        correct_psw = check_psw(s)

    return s


def update_string(char_list: list) -> str:
    for i in range(len(char_list) - 1, -1, -1):
        if char_list[i] > 122:
            char_list[i] = 97
            char_list[i - 1] += 1

        if char_list[i] in INVALID_NUMS:
            char_list[i] += 1
            char_list = reset_chars(char_list, i + 1)

    return char_list


def reset_chars(char_list: list, index: int) -> list:
    for i in range(index, len(char_list)):
        char_list[i] = 97

    return char_list


def check_psw(s: str) -> bool:
    is_straight = check_straight(s)
    valid_chars = check_valid_chars(s)
    pair_letter = check_pair_letters(s)

    return is_straight and valid_chars and pair_letter


def check_straight(s: str) -> bool:
    aux = [ord(c) for c in list(s)]
    count = 0
    has_straight = False
    for i in range(0, len(aux) - 1):
        if aux[i] + 1 == aux[i + 1]:
            count += 1
        else:
            count = 0

        if count >= 2:
            has_straight = True

    return has_straight


def check_valid_chars(s: str) -> bool:
    for c in INVALID:
        if c in s:
            return False

    return True


def check_pair_letters(s: str) -> bool:
    pair_count = 0
    last_pair = ""
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1] and s[i] != last_pair:
            pair_count += 1
            last_pair = s[i]

        if pair_count >= 2:
            return True

    return False


if __name__ == "__main__":
    main()
