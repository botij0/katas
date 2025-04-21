from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_val = max(nums) - k
        min_val = min(nums) + k
        return max(0, max_val - min_val)


if __name__ == "__main__":
    nums = [0, 10]
    k = 2
    print(Solution().smallestRangeI(nums, k))
