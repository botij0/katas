from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_product = 1
        result = [1] * n
        for i in range(n):
            result[i] *= pre_product
            pre_product *= nums[i]

        suf_prod = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suf_prod
            suf_prod *= nums[i]

        return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))
