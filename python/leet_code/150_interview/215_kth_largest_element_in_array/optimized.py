import heapq
from typing import List

# Actually, not optimized.
# Does the trick with heapq, which creates a heap based on a list and then the method .heappop deletes always the lower


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        return -nums[0]


if __name__ == "__main__":
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(Solution().findKthLargest(nums, k))
