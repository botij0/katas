from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s = len(set(candyType))
        n = len(candyType) // 2
        return min(s, n)


if __name__ == "__main__":
    candyType = [6, 6, 6, 6]
    print(Solution().distributeCandies(candyType))
