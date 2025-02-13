from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSort(nums, k)

    def quickSort(self, nums: List[int], k: int) -> List[int]:
        pivot = nums[len(nums) // 2]
        equals = []
        lowers = []
        highers = []
        for n in nums:
            if n < pivot:
                lowers.append(n)
            elif n == pivot:
                equals.append(n)
            else:
                highers.append(n)

        if len(highers) >= k:
            return self.quickSort(highers, k)
        elif len(highers) + len(equals) >= k:
            return pivot
        else:
            return self.quickSort(lowers, k - len(highers) - len(equals))


if __name__ == "__main__":
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(Solution().findKthLargest(nums, k))
