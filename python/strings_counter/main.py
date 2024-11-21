import re

def main():
    example = [
        "",
        "abc",
        "aaa\"aaa",
        "\x27"

    ]

    # Valid Solution ?
    print (sum(len(s[:-1]) - len(eval(s)) for s in open('puzzle_input.txt')))
    print (sum(2+s.count('\\')+s.count('"') for s in open('puzzle_input.txt')))



if __name__ == "__main__":
    main()
