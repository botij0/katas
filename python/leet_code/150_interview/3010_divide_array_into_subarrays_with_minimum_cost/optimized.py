from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        f = nums.pop(0)
        s = min(nums)
        nums.remove(s)
        t = min(nums)
        return f + s + t


if __name__ == "__main__":
    nums = [5, 4, 3]
    print(Solution().minimumCost(nums))
