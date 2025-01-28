class Solution(object):
    def removeDuplicates(self, nums: list) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = list(set(nums))
        return len(nums)


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    r = Solution().removeDuplicates(nums)
    print(r)
    print(nums)
