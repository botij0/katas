from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        n_dict = {}
        for i in range(n):
            if nums[i] in n_dict:
                aux = n_dict[nums[i]]
                n_dict[nums[i]] = [aux, i]
            else:
                n_dict[nums[i]] = i

        for i in range(n):
            if target - nums[i] in n_dict:
                if target - nums[i] == nums[i]:
                    if isinstance(n_dict[nums[i]], list):
                        return n_dict[nums[i]]
                    else:
                        continue
                else:
                    return [n_dict[nums[i]], n_dict[target - nums[i]]]

        return []


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))
