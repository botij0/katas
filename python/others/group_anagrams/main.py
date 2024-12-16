S = ["eat", "tea", "tan", "ate", "nat", "bat"]
J = ["vote", "please"]
P = ["debitcard", "badcredit"]


def main():
    print(group_anagrams(S))
    print(group_anagrams(J))
    print(group_anagrams(P))


def group_anagrams(words: list) -> list:
    groups_of_anagrams = []
    for word in words:
        is_grouped = False
        for group in groups_of_anagrams:
            aux = group[0]
            if check_anagram(aux, word):
                group.append(word)
                is_grouped = True
                break
        if not is_grouped:
            groups_of_anagrams.append([word])
    return groups_of_anagrams


def check_anagram(w1: str, w2: str) -> bool:
    return sorted(list(w1)) == sorted(list(w2))


if __name__ == "__main__":
    main()
