from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        return s.pop()


if __name__ == "__main__":
    nums = [2, 2, 1]
    print(Solution().singleNumber(nums))
