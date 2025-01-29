class Solution(object):
    def majorityElement(self, nums: list) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in set(nums):
            if nums.count(n) > len(nums) / 2:
                return n


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(nums))
