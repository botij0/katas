class Solution:
    def romanToInt(self, s: str) -> int:
        aux_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        last = -1
        for i in range(len(s) - 1, -1, -1):
            current = aux_dict[s[i]]
            if current >= last:
                total += current
            else:
                total -= current
            last = current

        return total


if __name__ == "__main__":
    s = "MCMXCIV"
    print(Solution().romanToInt(s))
