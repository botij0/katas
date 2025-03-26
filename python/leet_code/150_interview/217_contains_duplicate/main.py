from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().containsDuplicate(nums))
