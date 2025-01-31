class Solution(object):
    def numIslands(self, grid: list) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n_rows = len(grid)
        n_cols = len(grid[0])
        islands = []
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == "0":
                    continue

                if check_if_new_island(islands, i, j):
                    new_island = set()
                    calculate_island(i, j, n_rows, n_cols, grid, new_island)
                    islands.append(new_island)

        return len(islands)


def check_if_new_island(islands: set, i, j) -> bool:
    for island in islands:
        if (i, j) in island:
            return False
    return True


def calculate_island(i: int, j: int, n_rows: int, n_cols: int, grid: list, island: set):
    if (
        (i, j) in island
        or i <= -1
        or i >= n_rows
        or j <= -1
        or j >= n_cols
        or grid[i][j] == "0"
    ):
        return

    island.add((i, j))
    calculate_island(i - 1, j, n_rows, n_cols, grid, island)
    calculate_island(i + 1, j, n_rows, n_cols, grid, island)
    calculate_island(i, j - 1, n_rows, n_cols, grid, island)
    calculate_island(i, j + 1, n_rows, n_cols, grid, island)


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(Solution().numIslands(grid))
