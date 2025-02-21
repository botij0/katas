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
        indexes = [
            (i, j - 1),
            (i, j + 1),
            (i + 1, j),
            (i + 1, j + 1),
            (i + 1, j - 1),
            (i - 1, j),
            (i - 1, j - 1),
            (i - 1, j + 1),
        ]
        for index in indexes:
            new_i, new_j = index
            if new_i >= 0 and new_i < n_i and new_j >= 0 and new_j < n_j:
                count += board[new_i][new_j]

        return count

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
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    display_board(board)
    print()
    Solution().gameOfLife(board)
    display_board(board)
