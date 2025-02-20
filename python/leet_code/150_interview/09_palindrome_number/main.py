class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        aux = ""
        for i in range(len(s) - 1, -1, -1):
            aux += s[i]
        return aux == s


if __name__ == "__main__":
    x = 12
    print(Solution().isPalindrome(x))
