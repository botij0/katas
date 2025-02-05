from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        aux = sorted(prices)
        if prices == sorted(prices, reverse=True):
            return profit

        if prices.index(min(prices)) < prices.index(max(prices)):
            return max(prices) - min(prices)

        for i in range(len(prices) - 1):
            print(i)
            if profit >= max(prices[i:]) - min(prices[i:]):
                break
            if max(prices[i:]) - prices[i] > profit:
                profit = max(prices[i:]) - prices[i]

        return profit


if __name__ == "__main__":
    prices = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(prices))
