from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while nums:
            try:
                current = nums[0]
                nums.remove(current)
                nums.remove(current)
            except ValueError:
                return current


if __name__ == "__main__":
    nums = [2, 2, 1]
    print(Solution().singleNumber(nums))
