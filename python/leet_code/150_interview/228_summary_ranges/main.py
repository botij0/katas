from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        summ = []
        if len(nums) == 0:
            return summ
        last = nums[0]
        first = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != last + 1:
                if first != last:
                    summ.append(str(first) + "->" + str(last))
                else:
                    summ.append(str(first))

                first = nums[i]

            last = nums[i]

        if first != last:
            summ.append(str(first) + "->" + str(last))
        else:
            summ.append(str(first))

        return summ


if __name__ == "__main__":
    nums = [0, 2, 3, 4, 6, 8, 9]
    print(Solution().summaryRanges(nums))
