class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join([c for c in s.upper() if c.isalnum()])
        aux = new_s[::-1]
        return new_s == aux


if __name__ == "__main__":
    s = "0P"
    print(Solution().isPalindrome(s))
