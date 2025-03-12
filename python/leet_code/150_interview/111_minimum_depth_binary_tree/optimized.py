from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# To be OPTIMIZED it's better BFS than DFS in this problem.
# It is right because of the logic of BFS, check it out if not.
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))


if __name__ == "__main__":
    root = [2, None, 3, None, 4, None, 5, None, 6]
    print(Solution().minDepth(root))
