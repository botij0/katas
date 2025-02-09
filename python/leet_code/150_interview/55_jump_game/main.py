from typing import List, Dict


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final = len(nums) - 1
        can = False if final > 0 else True
        i = 0
        while i < final:
            print(i)
            if nums[i] + i >= final:
                can = True
                break

            i = self.get_next_step(nums, i)
            if i == -1:
                break

        for i in range(final):
            if nums[i] == 0:
                break
            if nums[i] + i >= final:
                can = True
                break
        return can

    def get_next_step(self, nums: List[int], current: int) -> int:
        if nums[current] == 0:
            return -1

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
    nums = [4, 2, 0, 0, 1, 1, 4, 4, 4, 0, 4, 0]
    print(Solution().canJump(nums))
