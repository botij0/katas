class Solution(object):
    def rotate(self, nums: list, k: int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        aux = len(nums) - k if k < len(nums) else len(nums) - (k % len(nums))
        nums1 = nums[aux:]
        print(nums1)
        nums[:] = nums1 + nums[:aux]


if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 4
    Solution().rotate(nums, k)
    print(nums)
