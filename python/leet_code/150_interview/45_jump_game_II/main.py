from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        final = len(nums) - 1
        can = 0
        i = 0
        while i < final:
            if nums[i] == 0:
                break
            if nums[i] + i >= final:
                can += 1
                break

            i = self.get_next_step(nums, i)
            can += 1
            if i == -1:
                break
        return can

    def get_next_step(self, nums: List[int], current: int) -> int:
        val = nums[current]
        i = 1
        max_val = 0
        i_val = -1
        while i <= val:
            if (nums[current + i] + i) >= max_val:
                max_val = nums[current + i] + i
                i_val = current + i
            i += 1
        return -1 if max_val == 0 else i_val


if __name__ == "__main__":
    nums = [2, 3, 0, 1, 4]
    print(Solution().jump(nums))
