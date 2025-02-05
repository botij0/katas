from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lower = 100000000
        for n in prices:
            if n < lower:
                lower = n
                continue
            if n - lower > profit:
                profit = n - lower

        return profit


if __name__ == "__main__":
    prices = [2, 1, 4]
    print(Solution().maxProfit(prices))
