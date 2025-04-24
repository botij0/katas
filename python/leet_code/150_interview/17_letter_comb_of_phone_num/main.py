from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        r = []
        if digits == "":
            return r
        letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def backtrack(i: int, comb: str):
            if i == len(digits):
                r.append(comb[:])
                return

            for letter in letters[digits[i]]:
                backtrack(i + 1, comb + letter)

        backtrack(0, "")
        return r


if __name__ == "__main__":
    digits = "23"
    print(Solution().letterCombinations(digits))
