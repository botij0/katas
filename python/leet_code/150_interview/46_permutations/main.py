from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        totals = []
        self.get_permutation(totals, nums, [])
        return totals

    def get_permutation(self, totals: list, remaining: list, current: list):
        if len(remaining) == 1:
            totals.append(current + remaining)

        for i in range(len(remaining)):
            self.get_permutation(
                totals, remaining[i + 1 :] + remaining[:i], current + [remaining[i]]
            )


if __name__ == "__main__":
    nums = [1, 2]
    print(Solution().permute(nums))
