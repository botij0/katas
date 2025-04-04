from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r = []
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"

        for w in words:
            aux = w.lower()
            f1 = True
            f2 = True
            f3 = True
            for c in aux:
                if f1:
                    if c not in r1:
                        f1 = False
                if f2:
                    if c not in r2:
                        f2 = False
                if f3:
                    if c not in r3:
                        f3 = False

            if f1 or f2 or f3:
                r.append(w)

        return r


if __name__ == "__main__":
    words = ["Hello", "Alaska", "Dad", "Peace"]
    print(Solution().findWords(words))
