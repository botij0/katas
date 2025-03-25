class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = set()
        while True:
            if n in numbers:
                return False
            else:
                numbers.add(n)

            n = self.get_new_n(n)
            print(n)

            if n == 1:
                break

        return True

    def get_new_n(self, n: int) -> int:
        r = 0
        while n > 0:
            aux = n % 10
            r += aux * aux
            n //= 10

        return r


if __name__ == "__main__":
    n = 2
    print(Solution().isHappy(n))
