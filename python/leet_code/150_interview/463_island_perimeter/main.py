from typing import List


TOTAL = 0


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def check_square(i: int, j: int, n: int, m: int):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return 0
            return 1

        total = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    current = 4
                    current -= check_square(i, j + 1, n, m)
                    current -= check_square(i, j - 1, n, m)
                    current -= check_square(i + 1, j, n, m)
                    current -= check_square(i - 1, j, n, m)
                    total += current

        return total


if __name__ == "__main__":
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(Solution().islandPerimeter(grid))
