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
    if (i, j) in island:
        return

    island.add((i, j))
    if is_a_corner(i, j, n_cols, n_rows):
        if i == 0 and j == 0:
            if n_rows > 1 and grid[i + 1][j] == "1":
                calculate_island(i + 1, j, n_rows, n_cols, grid, island)
            if n_cols > 1 and grid[i][j + 1] == "1":
                calculate_island(i, j + 1, n_rows, n_cols, grid, island)
        elif i == 0 and j == n_cols - 1:
            if n_rows > 1 and grid[i + 1][j] == "1":
                calculate_island(i + 1, j, n_rows, n_cols, grid, island)
            if n_cols > 1 and grid[i][j - 1] == "1":
                calculate_island(i, j - 1, n_rows, n_cols, grid, island)
        elif i == n_rows - 1 and j == 0:
            if n_rows > 1 and grid[i - 1][j] == "1":
                calculate_island(i - 1, j, n_rows, n_cols, grid, island)
            if n_cols > 1 and grid[i][j + 1] == "1":
                calculate_island(i, j + 1, n_rows, n_cols, grid, island)
        elif i == n_rows - 1 and j == n_cols - 1:
            if n_rows > 1 and grid[i - 1][j] == "1":
                calculate_island(i - 1, j, n_rows, n_cols, grid, island)
            if n_cols > 1 and grid[i][j - 1] == "1":
                calculate_island(i, j - 1, n_rows, n_cols, grid, island)

    elif is_an_edge(i, j, n_cols, n_rows):
        if i == 0:
            if n_rows > 1 and grid[i + 1][j] == "1":
                calculate_island(i + 1, j, n_rows, n_cols, grid, island)
            if n_cols > 1 and grid[i][j + 1] == "1":
                calculate_island(i, j + 1, n_rows, n_cols, grid, island)
            if n_cols > 1 and grid[i][j - 1] == "1":
                calculate_island(i, j - 1, n_rows, n_cols, grid, island)
        if i == n_rows - 1:
            if n_rows > 1 and grid[i - 1][j] == "1":
                calculate_island(i - 1, j, n_rows, n_cols, grid, island)
            if n_cols > 1 and grid[i][j + 1] == "1":
                calculate_island(i, j + 1, n_rows, n_cols, grid, island)
            if n_cols > 1 and grid[i][j - 1] == "1":
                calculate_island(i, j - 1, n_rows, n_cols, grid, island)
        if j == 0:
            if n_rows > 1 and grid[i - 1][j] == "1":
                calculate_island(i - 1, j, n_rows, n_cols, grid, island)
            if n_cols > 1 and grid[i][j + 1] == "1":
                calculate_island(i, j + 1, n_rows, n_cols, grid, island)
            if n_rows > 1 and grid[i + 1][j] == "1":
                calculate_island(i + 1, j, n_rows, n_cols, grid, island)
        if j == n_cols - 1:
            if n_rows > 1 and grid[i - 1][j] == "1":
                calculate_island(i - 1, j, n_rows, n_cols, grid, island)
            if n_cols > 1 and grid[i][j - 1] == "1":
                calculate_island(i, j - 1, n_rows, n_cols, grid, island)
            if n_rows > 1 and grid[i + 1][j] == "1":
                calculate_island(i + 1, j, n_rows, n_cols, grid, island)

    else:
        if grid[i][j + 1] == "1":
            calculate_island(i, j + 1, n_rows, n_cols, grid, island)
        if grid[i][j - 1] == "1":
            calculate_island(i, j - 1, n_rows, n_cols, grid, island)
        if grid[i + 1][j] == "1":
            calculate_island(i + 1, j, n_rows, n_cols, grid, island)
        if grid[i - 1][j] == "1":
            calculate_island(i - 1, j, n_rows, n_cols, grid, island)


def is_a_corner(i: int, j: int, n_cols: int, n_rows: int) -> bool:
    return (i == 0 and (j == 0 or j == n_cols - 1)) or (
        i == n_rows - 1 and (j == 0 or j == n_cols - 1)
    )


def is_an_edge(i: int, j: int, n_cols: int, n_rows: int) -> bool:
    return i == 0 or j == 0 or i == n_rows - 1 or j == n_cols - 1


if __name__ == "__main__":
    grid = [["1", "1"]]
    print(Solution().numIslands(grid))
