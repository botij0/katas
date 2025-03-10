from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        aux = 1
        index = len(digits) - 1
        while aux == 1:
            if index < 0:
                digits.insert(0, aux)
                break
            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1
                aux = 0
            index -= 1

        return digits


if __name__ == "__main__":
    digits = [9, 9, 9]
    print(Solution().plusOne(digits))
