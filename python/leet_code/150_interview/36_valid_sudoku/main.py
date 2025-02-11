from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        table = self.build_hash_table(board)
        if table == {}:
            return False

        return self.check_table(table)

    def check_table(self, table: dict) -> bool:
        return (
            self.check_rows(table["rows"])
            and self.check_cols(table["cols"])
            and self.check_cells(table["cells"])
        )

    def check_rows(self, rows: List[List[str]]) -> bool:
        for row in rows:
            if len(row) > len(set(row)):
                return False
        return True

    def check_cols(self, cols: List[List[str]]) -> bool:
        for col in cols:
            if len(col) > len(set(col)):
                return False
        return True

    def check_cells(self, cells: List[List[str]]) -> bool:
        for cell in cells:
            if len(cell) > len(set(cell)):
                return False
        return True

    def build_hash_table(self, board: List[List[str]]) -> dict:
        table = {
            "rows": [[], [], [], [], [], [], [], [], []],
            "cols": [[], [], [], [], [], [], [], [], []],
            "cells": [[], [], [], [], [], [], [], [], []],
        }
        VALID_INPUT = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        index = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] not in VALID_INPUT:
                    return {}

                if board[i][j] != ".":
                    table["rows"][i].append(board[i][j])
                    table["cols"][j].append(board[i][j])
                    table["cells"][(2 * (index // 3)) + (i // 3) + (j // 3)].append(
                        board[i][j]
                    )
            index += 1
        return table


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
