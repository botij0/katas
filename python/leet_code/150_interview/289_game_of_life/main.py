from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        mod = {}
        n_i = len(board)
        n_j = len(board[0])
        for i in range(n_i):
            for j in range(n_j):
                live_cells = self.get_neighbors(board, i, j, n_i, n_j)
                if board[i][j] == 0:
                    if live_cells == 3:
                        mod[(i, j)] = 1
                else:
                    if live_cells < 2:
                        mod[(i, j)] = 0
                    elif live_cells < 4:
                        mod[(i, j)] = 1
                    else:
                        mod[(i, j)] = 0

        return self.update_board(board, mod)

    def get_neighbors(
        self, board: List[List[int]], i: int, j: int, n_i: int, n_j: int
    ) -> int:
        count = 0

        if n_i == 1 and n_j == 1:
            return count

        if self.is_corner(board, i, j, n_i, n_j):
            if n_i == 1 and j == 0:
                count += board[i][j + 1]
            elif n_i == 1 and j == n_j - 1:
                count += board[i][j - 1]
            elif n_j == 1 and i == 0:
                count += board[i + 1][j]
            elif n_j == 1 and i == n_i - 1:
                count += board[i - 1][j]
            elif i == 0 and j == 0:
                count += board[i][j + 1]
                count += board[i + 1][j]
                count += board[i + 1][j + 1]
            elif i == 0 and j == n_j - 1:
                count += board[i][j - 1]
                count += board[i + 1][j]
                count += board[i + 1][j - 1]
            elif i == n_i - 1 and j == 0:
                count += board[i - 1][j]
                count += board[i - 1][j + 1]
                count += board[i][j + 1]
            else:
                count += board[i - 1][j]
                count += board[i - 1][j - 1]
                count += board[i][j - 1]

        elif self.is_border(board, i, j, n_i, n_j):
            if n_i == 1:
                count += board[i][j + 1]
                count += board[i][j - 1]
            elif n_j == 1:
                count += board[i + 1][j]
                count += board[i - 1][j]
            elif i == 0:
                count += board[i][j + 1]
                count += board[i][j - 1]
                count += board[i + 1][j]
                count += board[i + 1][j + 1]
                count += board[i + 1][j - 1]
            elif i == n_i - 1:
                count += board[i][j + 1]
                count += board[i][j - 1]
                count += board[i - 1][j]
                count += board[i - 1][j + 1]
                count += board[i - 1][j - 1]
            elif j == 0:
                count += board[i][j + 1]
                count += board[i - 1][j]
                count += board[i + 1][j]
                count += board[i + 1][j + 1]
                count += board[i - 1][j + 1]
            else:
                count += board[i][j - 1]
                count += board[i - 1][j]
                count += board[i + 1][j]
                count += board[i + 1][j - 1]
                count += board[i - 1][j - 1]
        else:
            count += board[i][j - 1]
            count += board[i][j + 1]
            count += board[i + 1][j]
            count += board[i + 1][j - 1]
            count += board[i + 1][j + 1]
            count += board[i - 1][j]
            count += board[i - 1][j + 1]
            count += board[i - 1][j - 1]

        return count

    def is_corner(
        self, board: List[List[int]], i: int, j: int, n_i: int, n_j: int
    ) -> bool:
        return (
            (i == 0 and j == 0)
            or (i == n_i - 1 and j == 0)
            or (i == 0 and j == (n_j - 1))
            or (i == (n_i - 1) and j == n_j - 1)
        )

    def is_border(
        self, board: List[List[int]], i: int, j: int, n_i: int, n_j: int
    ) -> bool:
        return i == 0 or i == n_i - 1 or j == 0 or j == n_j - 1

    def update_board(self, board: List[List[int]], mod: dict):
        for k, v in mod.items():
            i, j = k
            board[i][j] = v


def display_board(board: List[List[int]]):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()


if __name__ == "__main__":
    board = [[1], [0], [0], [1], [0], [0], [1], [0], [0], [1]]
    display_board(board)
    print()
    Solution().gameOfLife(board)
    display_board(board)
