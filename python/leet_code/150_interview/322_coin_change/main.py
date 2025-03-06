from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [amount + 1] * (amount + 1)
        min_coins[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    min_coins[i] = min(min_coins[i], 1 + min_coins[i - c])

        return min_coins[-1] if min_coins[-1] != amount + 1 else -1


if __name__ == "__main__":
    coins = [1, 5]
    amount = 10
    print(Solution().coinChange(coins, amount))
