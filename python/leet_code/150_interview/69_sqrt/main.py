class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        initial = x // (x - (x // 2))
        r = 1

        while r <= x:
            r = initial * initial
            initial += 1

        return initial - 2


if __name__ == "__main__":
    x = 8
    print(Solution().mySqrt(x))
