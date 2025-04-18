from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r = []

        for num in range(left, right + 1):
            aux = num
            is_self_dividing = True

            while aux > 0:
                digit = aux % 10

                if digit == 0 or num % digit != 0:
                    is_self_dividing = False
                    break

                aux //= 10

            if is_self_dividing:
                r.append(num)

        return r


if __name__ == "__main__":
    left = 1
    right = 22
    print(Solution().selfDividingNumbers(left, right))
