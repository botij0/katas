class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        aux = {}
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in aux.keys():
                if words[i] in aux.values():
                    return False
                aux[pattern[i]] = words[i]
            else:
                if aux[pattern[i]] != words[i]:
                    return False

        return True


if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat fish"
    print(Solution().wordPattern(pattern, s))
