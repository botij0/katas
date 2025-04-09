class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)


if __name__ == "__main__":
    n = 3
    print(Solution().fib(n))
