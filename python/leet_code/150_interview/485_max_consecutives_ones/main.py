from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        n_con_max = 0
        for n in nums:
            if n == 0:
                n_con_max = max(current, n_con_max)
                current = 0
            else:
                current += 1

        return max(current, n_con_max)


if __name__ == "__main__":
    nums = [1, 0, 1, 1, 0, 1]
    print(Solution().findMaxConsecutiveOnes(nums))
