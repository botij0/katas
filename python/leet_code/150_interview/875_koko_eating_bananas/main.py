from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            total_time = self.get_total_time(piles, mid)

            if total_time > h:
                left = mid + 1
            else:
                right = mid

        return left

    def get_total_time(self, piles: List[int], speed: int) -> int:
        total_time = 0
        for pile in piles:
            total_time += pile // speed
            total_time += 1 if pile % speed != 0 else 0
        return total_time


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    print(Solution().minEatingSpeed(piles, h))
