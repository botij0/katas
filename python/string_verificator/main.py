def main():
    file_content = read_file("puzzle_input.txt")
    s_list = file_content.split("\n")
    nice_strings = 0
    for s in s_list:
        if new_checker(s):
            nice_strings += 1
    print(nice_strings)


def new_checker(s: str) -> bool:
    return check_letter_between(s) and check_pair(s)


def check_letter_between(s: str) -> bool:
    last_character = s[1]
    last_2_character = s[0]
    for i in range(2, len(s)):
        if last_2_character == s[i]:
            return True
        last_2_character = last_character
        last_character = s[i]
    return False


def check_pair(s: str) -> bool:
    pares = [s[i : i + 2] for i in range(0, len(s) - 1)]
    overlaping_flag = False
    last_par = ""
    for par in pares:
        if par == last_par:
            overlaping_flag = True
        last_par = par

    return len(pares) > len(set(pares)) and not overlaping_flag


def checker_pair_letter_no_overlaping(s: str) -> bool:
    twice_letter_flag = check_twice_letter(s)
    s_list = list(s)
    return twice_letter_flag is False and len(s_list) > len(set(s_list))


def checker_string(s: str) -> bool:
    no_contains_flag = check_no_contains(s)
    vowels_count = 0
    last_character = ""
    twice_letter_flag = False
    for c in s:
        vowels_count += check_vowel(c)
        if last_character == c:
            twice_letter_flag = True
        last_character = c

    three_vowels_flag = vowels_count >= 3

    return three_vowels_flag and twice_letter_flag and no_contains_flag


def check_vowel(c: str) -> int:
    vowels_list = ["a", "e", "i", "o", "u"]
    if c in vowels_list:
        return 1
    return 0


def check_twice_letter(s: str) -> bool:
    last_character = ""
    for c in s:
        if last_character == c:
            return True
        last_character = c

    return False


def check_no_contains(s: str) -> bool:
    return (
        s.find("ab") == -1
        and s.find("cd") == -1
        and s.find("pq") == -1
        and s.find("xy") == -1
    )


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
