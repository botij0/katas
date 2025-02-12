from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = self.get_start(gas, cost)
        print(start)
        if start == -1:
            return -1

        tank = gas[start]
        i = start + 1 if start < len(cost) - 1 else 0
        j = i - 1 if i != 0 else len(gas) - 1
        # while True:
        #     if tank - cost[j] < 0:
        #         return -1

        #     tank += gas[i] - cost[j]

        #     if i == start:
        #         break
        #     i = i + 1 if i + 1 < len(cost) else 0
        #     j = j + 1 if j + 1 < len(cost) else 0

        return start

    def get_start(self, gas: List[int], cost: List[int]) -> int:
        max_diff = -1
        better_start = -1
        for i in range(len(gas)):
            if gas[i] - cost[i] >= 0:
                j = i + 1 if i < len(gas) - 1 else 0
                suma = gas[i] - cost[i] + gas[j] - cost[j]
                if suma > max_diff:
                    max_diff = suma
                    better_start = i

        return better_start


if __name__ == "__main__":
    gas = [6, 1, 4, 3, 5]
    cost = [3, 8, 2, 4, 2]
    print(sum(gas) - sum(cost) + (gas[4] - cost[0]))
    # print(Solution().canCompleteCircuit(gas, cost))
