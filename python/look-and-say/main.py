N_ITER = 50
PUZZLE_INPUT = "1113222113"
EXAMPLE_INPUT = "1"


def main():
    s = PUZZLE_INPUT
    for i in range(0, N_ITER):
        s = get_next_sequence(s)

    print(len(s))


def get_next_sequence(s: str) -> str:
    partial_count = 0
    last_char = s[0]
    final_str = ""
    for c in s:
        if c == last_char:
            partial_count += 1
        else:
            final_str += str(partial_count) + last_char
            partial_count = 1
        last_char = c

    final_str += str(partial_count) + c
    return final_str


if __name__ == "__main__":
    main()
