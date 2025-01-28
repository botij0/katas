class Solution(object):
    def removeDuplicates(self, nums: list) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in nums:
            while nums.count(n) > 2:
                nums.remove(n)
        return len(nums)


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    r = Solution().removeDuplicates(nums)
    print(r)
    print(nums)
