from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.find_max_depth(root, 0)

    def find_max_depth(self, root: Optional[TreeNode], depth: int):
        if root is None:
            return depth

        depth_l = self.find_max_depth(root.left, depth + 1)
        depth_r = self.find_max_depth(root.right, depth + 1)
        return max(depth_l, depth_r)


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
    arr = [3, 9, 20, None, None, 15, 7]
    root = build_tree(arr)
    print(Solution().maxDepth(root))
