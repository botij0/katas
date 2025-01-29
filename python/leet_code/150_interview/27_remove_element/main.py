class Solution(object):
    def removeElement(self, nums: list, val: int) -> int:
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        try:
            while True:
                nums.remove(val)
        except ValueError:
            return len(nums)


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    r = Solution().removeElement(nums, val)
    print(r)
    print(nums)
