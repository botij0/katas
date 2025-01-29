class Solution(object):
    def minSubArrayLen(self, target: int, nums: list) -> int:
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        sumOfCurrentWindow = 0
        res = len(nums) + 1

        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]

            while sumOfCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1

        return res if res != len(nums) + 1 else 0


if __name__ == "__main__":
    target = 11
    nums = [1, 2, 3, 4, 5]
    print(Solution().minSubArrayLen(target, nums))
