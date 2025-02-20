class Solution:
    def isPalindrome(self, x: int) -> bool:
        aux = 0
        temp = x
        while temp > 0:
            digit = temp % 10
            aux = aux * 10 + digit
            temp //= 10

        return aux == x


if __name__ == "__main__":
    x = 112
    print(Solution().isPalindrome(x))
