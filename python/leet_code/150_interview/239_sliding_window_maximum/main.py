from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = []
        current_max = max(nums[0:k])
        current_max_index = nums[0:k].index(current_max)
        for i in range(len(nums)):
            if current_max_index < i:
                current_max = max(nums[i : k + i])
                current_max_index = nums[i : k + i].index(current_max) + i
            else:
                if nums[i] > current_max:
                    current_max = nums[i]

            arr.append(current_max)
        return arr


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    # print(nums[0:k])
    print(Solution().maxSlidingWindow(nums, k))
