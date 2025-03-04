from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.special_binary_search(nums, target)

    def special_binary_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        if target <= nums[-1]:
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid

                if nums[mid] < target or (nums[mid] > target and nums[mid] > nums[-1]):
                    left = mid + 1
                else:
                    right = mid - 1
        else:
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid

                if nums[mid] > target or (nums[mid] < target and nums[mid] < nums[-1]):
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    print(Solution().search(nums, target))
