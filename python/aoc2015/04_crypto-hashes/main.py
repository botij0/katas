import hashlib

PUZZLE_INPUT = "iwrupvqb"


def main():
    init_hash = get_md5(PUZZLE_INPUT)
    i = 0
    while not check_hash(init_hash):
        init_hash = get_md5(PUZZLE_INPUT + str(i))
        i += 1

    print("Solution: " + str(i - 1))
    print("Final Hash: " + init_hash)


def check_hash(hash_input: str) -> bool:
    return hash_input.startswith("000000")


def get_md5(puzzle_input: str) -> str:
    hash_md5 = hashlib.md5()
    hash_md5.update(puzzle_input.encode("utf-8"))
    return hash_md5.hexdigest()


if __name__ == "__main__":
    main()
