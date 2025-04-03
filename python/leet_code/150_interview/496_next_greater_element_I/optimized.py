from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for n in nums2:
            while stack and n > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = n
            stack.append(n)

        return [next_greater.get(i, -1) for i in nums1]


if __name__ == "__main__":
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(Solution().nextGreaterElement(nums1, nums2))
