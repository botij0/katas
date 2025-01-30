class Solution(object):
    def numIslands(self, grid: list) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n_rows = len(grid)
        n_cols = len(grid[0])
        res = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == "1":
                    calculate_island(i, j, n_rows, n_cols, grid)
                    res += 1

        return res


def calculate_island(i: int, j: int, n_rows: int, n_cols: int, grid: list):
    if i <= -1 or i >= n_rows or j <= -1 or j >= n_cols or grid[i][j] == "0":
        return

    grid[i][j] = "0"
    calculate_island(i - 1, j, n_rows, n_cols, grid)
    calculate_island(i + 1, j, n_rows, n_cols, grid)
    calculate_island(i, j - 1, n_rows, n_cols, grid)
    calculate_island(i, j + 1, n_rows, n_cols, grid)


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(Solution().numIslands(grid))
