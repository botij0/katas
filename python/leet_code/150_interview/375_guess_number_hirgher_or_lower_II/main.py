class Solution:
    def getMoneyAmount(self, n: int) -> int:
        first_try = int(n * 0.7)

        return self.build_tree(n, first_try)

    def build_tree(self, n: int, first_try: int):
        tree = {first_try: []}
        self.build_branch(first_try, tree, n, first_try // 2)
        self.build_branch(first_try, tree, n, ((n - first_try) // 2) + 1)
        return tree

    def build_branch(self, father: int, tree: dict, n: int, new_value: int):
        if new_value <= 0 or new_value >= n:
            return

        tree[father].append(new_value)
        tree[new_value] = []

        self.build_branch(new_value, tree, n, new_value // 2)
        self.build_branch(new_value, tree, n, ((n + new_value) // 2) + 1)


if __name__ == "__main__":
    n = 10
    print(Solution().getMoneyAmount(n))
