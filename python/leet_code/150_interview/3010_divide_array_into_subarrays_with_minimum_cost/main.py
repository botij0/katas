from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def get_all_subarrays(start, k=3):
            if k == 1:
                return [[nums[start:]]]

            partitions = []
            for i in range(start + 1, len(nums) - k + 2):
                first_part = nums[start:i]
                for rest in get_all_subarrays(i, k - 1):
                    partitions.append([first_part] + rest)

            return partitions

        def get_all_cost_partitions(partitions, results):
            for partition in partitions:
                total = 0
                for arr in partition:
                    total += arr[0]
                results.append(total)

        partitions = get_all_subarrays(0)
        results = []
        get_all_cost_partitions(partitions, results)

        return min(results)


if __name__ == "__main__":
    nums = [5, 4, 3]
    print(Solution().minimumCost(nums))
