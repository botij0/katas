from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        n = len(piles)
        speed = piles[n // 2]
        total_time = self.get_total_time(piles, speed)
        if total_time == h:
            return speed
        elif total_time > h:
            while total_time > h:
                speed += total_time // h
                total_time = self.get_total_time(piles, speed)
        else:
            while total_time <= h:
                speed -= h // total_time
                total_time = self.get_total_time(piles, speed)

        return speed

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
