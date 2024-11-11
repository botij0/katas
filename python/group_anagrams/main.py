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
    w1_list = list(w1)
    w2_list = list(w2)

    w1_list.sort()
    w2_list.sort()

    return w1_list == w2_list


if __name__ == "__main__":
    main()
