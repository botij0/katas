from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) < 2:
            return TreeNode(nums[0])
        index_center = len(nums) // 2
        center = nums[index_center]
        left_array = nums[:index_center]
        right_array = nums[index_center + 1 :]
        print(left_array, right_array)
        return TreeNode(
            center,
            left=self.sortedArrayToBST(left_array) if len(left_array) > 0 else None,
            right=self.sortedArrayToBST(right_array) if len(right_array) > 0 else None,
        )


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    print(Solution().sortedArrayToBST(nums))
