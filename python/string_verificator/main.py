def main():
    file_content = read_file("puzzle_input.txt")
    s_list = file_content.split("\n")
    nice_strings = 0
    for s in s_list:
        if checker_string(s):
            nice_strings += 1
    print(nice_strings)


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
