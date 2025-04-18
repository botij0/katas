from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r = []
        for i in range(left, right + 1):
            aux = i
            f = True
            while aux > 0:
                j = aux % 10
                if j == 0 or i % j != 0:
                    f = False
                    break
                aux //= 10

            if f:
                r.append(i)

        return r


if __name__ == "__main__":
    left = 1
    right = 22
    print(Solution().selfDividingNumbers(left, right))
