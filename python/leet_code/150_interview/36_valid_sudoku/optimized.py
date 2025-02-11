from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[], [], [], [], [], [], [], [], []]
        cols = [[], [], [], [], [], [], [], [], []]
        cells = [[], [], [], [], [], [], [], [], []]

        VALID_INPUT = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        index = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue

                if board[i][j] not in VALID_INPUT:
                    return False

                # check Row
                if board[i][j] in rows[i]:
                    return False

                # check Cols
                if board[i][j] in cols[j]:
                    return False

                if board[i][j] in cells[(2 * (index // 3)) + (i // 3) + (j // 3)]:
                    return False

                rows[i].append(board[i][j])
                cols[j].append(board[i][j])
                cells[(2 * (index // 3)) + (i // 3) + (j // 3)].append(board[i][j])

            index += 1

        return True


if __name__ == "__main__":
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(Solution().isValidSudoku(board))
