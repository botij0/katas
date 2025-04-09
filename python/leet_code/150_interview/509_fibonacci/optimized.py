class Solution:
    def fib(self, n: int, aux: dict = {}) -> int:
        if n < 2:
            return n

        if n in aux:
            return aux[n]

        r = self.fib(n - 1, aux) + self.fib(n - 2, aux)
        aux[n] = r
        return r


if __name__ == "__main__":
    n = 3
    print(Solution().fib(n))
