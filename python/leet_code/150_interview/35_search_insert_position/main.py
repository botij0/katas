from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mid_index = n // 2
        if nums[mid_index] == target:
            return mid_index
        if nums[mid_index] > target:
            for i in range(n):
                if nums[i] >= target:
                    return i
        elif nums[mid_index] < target:
            for i in range(mid_index, n):
                if nums[i] >= target:
                    return i

            return n


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 7
    print(Solution().searchInsert(nums, target))
