from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        manum = max(nums)
        minum = min(nums)

        aux = manum - minum
        x = minum + aux if aux <= k else minum + k
        y = x if manum - x <= k else manum - k
        return abs(x - y)


if __name__ == "__main__":
    nums = [0, 10]
    k = 2
    print(Solution().smallestRangeI(nums, k))
