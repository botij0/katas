class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = set()
        while n != 1:
            if n in numbers:
                return False

            numbers.add(n)
            n = self.get_new_n(n)

            if n == 1:
                break

        return True

    def get_new_n(self, n: int) -> int:
        r = 0
        while n > 0:
            r += (n % 10) ** 2
            n //= 10

        return r


if __name__ == "__main__":
    n = 2
    print(Solution().isHappy(n))
