from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        aux = 0
        for i in range(n + 1):
            aux += i
        x = sum(nums)
        print(x, aux)
        return aux - x


if __name__ == "__main__":
    nums = [3, 0, 1]
    print(Solution().missingNumber(nums))
