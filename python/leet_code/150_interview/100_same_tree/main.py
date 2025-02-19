from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        if p and q and p.val != q.val:
            return False

        left_branch = self.isSameTree(p.left, q.left)
        right_branch = self.isSameTree(p.right, q.right)

        return right_branch and left_branch
