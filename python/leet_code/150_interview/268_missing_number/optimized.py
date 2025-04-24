from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums) * (len(nums) + 1)) // 2 - sum(nums)


if __name__ == "__main__":
    nums = [3, 0, 1]
    print(Solution().missingNumber(nums))
