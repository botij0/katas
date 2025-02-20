import math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        total = math.factorial(n)

        n_zeroes = 0
        r = 0
        while r == 0:
            r = total % 10
            if r == 0:
                n_zeroes += 1
            total = total // 10
        return n_zeroes


if __name__ == "__main__":
    n = 25
    print(Solution().trailingZeroes(n))
