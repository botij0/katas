from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        totals = []
        uniques = set()
        self.get_permutation(totals, nums, [], uniques)
        return totals

    def get_permutation(
        self, totals: list, remaining: list, current: list, uniques: set
    ):
        if len(remaining) == 1:
            perm_str = str(current + remaining)
            if perm_str not in uniques:
                uniques.add(perm_str)
                totals.append(current + remaining)
            return

        for i in range(len(remaining)):
            self.get_permutation(
                totals,
                remaining[i + 1 :] + remaining[:i],
                current + [remaining[i]],
                uniques,
            )


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(Solution().permute(nums))
