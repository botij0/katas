from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(
        self, root: Optional[TreeNode], targetSum: int, current: int = 0
    ) -> bool:
        if not root:
            return False
        if current + root.val == targetSum and self.is_leaf(root):
            return True

        current += root.val

        if root.left:
            r = self.hasPathSum(root.left, targetSum, current)
            if r:
                return True

        if root.right:
            r = self.hasPathSum(root.right, targetSum, current)
            if r:
                return True

        return False

    def is_leaf(self, node: TreeNode) -> bool:
        return True if not node.left and not node.right else False


def insert_level_order(arr: list, root: Optional[TreeNode], i: int, n: int) -> TreeNode:
    """Función para construir un árbol binario a partir de un array en orden por niveles."""
    if i < n and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root


def build_tree(arr: list) -> TreeNode:
    """Construye el árbol binario a partir de un array."""
    return insert_level_order(arr, None, 0, len(arr))


if __name__ == "__main__":
    root = [8, 9, -6, None, None, 5, 9]
    root = build_tree(root)
    target_sum = 7
    print(Solution().hasPathSum(root, target_sum))
