from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        index_left = 0
        index_right = len(height) - 1
        left_max = height[index_left]
        right_max = height[index_right]
        water = 0

        while index_left < index_right:
            if left_max < right_max:
                index_left += 1
                left_max = max(left_max, height[index_left])
                water += left_max - height[index_left]
            else:
                index_right -= 1
                right_max = max(right_max, height[index_right])
                water += right_max - height[index_right]

        return water


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))
