class Solution:
    def trailingZeroes(self, n: int) -> int:
        n_zeroes = 0
        while n > 0:
            n //= 5
            n_zeroes += n
        return n_zeroes


if __name__ == "__main__":
    n = 25
    print(Solution().trailingZeroes(n))
