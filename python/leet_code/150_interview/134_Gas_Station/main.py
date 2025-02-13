from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        start = 0
        remain_gas = 0
        for i in range(len(gas)):
            remain_gas += gas[i] - cost[i]
            if remain_gas < 0:
                remain_gas = 0
                start = i + 1

        return start


if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(Solution().canCompleteCircuit(gas, cost))  # 3
