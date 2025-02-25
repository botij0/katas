class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(list(s.strip().split(" "))[-1])


if __name__ == "__main__":
    s = "   fly me   to   the moon  "
    print(Solution().lengthOfLastWord(s))
