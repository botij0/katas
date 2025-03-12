from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode], depth: int = 1) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return depth

        l_depth = self.minDepth(root.left, depth + 1) if root.left else 100000000000
        r_depth = self.minDepth(root.right, depth + 1) if root.right else 10000000000000

        return min(l_depth, r_depth)


if __name__ == "__main__":
    root = [2, None, 3, None, 4, None, 5, None, 6]
    print(Solution().minDepth(root))
