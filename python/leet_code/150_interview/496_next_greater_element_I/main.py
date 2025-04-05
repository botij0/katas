from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def find_next_greater(arr: List[int], x) -> int:
            for n in arr:
                if n > x:
                    return n
            return -1

        r = []
        for n in nums1:
            i = nums2.index(n)
            r.append(find_next_greater(nums2[i:], n))

        return r


if __name__ == "__main__":
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(Solution().nextGreaterElement(nums1, nums2))
