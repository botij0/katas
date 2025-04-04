from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def check_rows(w: str) -> bool:
            f1 = True
            f2 = True
            f3 = True
            r1 = "qwertyuiop"
            r2 = "asdfghjkl"
            r3 = "zxcvbnm"
            for c in w:
                if f1:
                    if c not in r1:
                        f1 = False
                if f2:
                    if c not in r2:
                        f2 = False
                if f3:
                    if c not in r3:
                        f3 = False
            return f1 or f2 or f3

        r = []
        for w in words:
            if check_rows(w.lower()):
                r.append(w)

        return r


if __name__ == "__main__":
    words = ["Hello", "Alaska", "Dad", "Peace"]
    print(Solution().findWords(words))
