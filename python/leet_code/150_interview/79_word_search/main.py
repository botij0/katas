from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        alredy = set()
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                self.find_word(board, i, j, word, alredy, n, m)
                print(alredy)
                if len(alredy) == len(word):
                    return True
                alredy = set()
        return False

    def find_word(
        self,
        board: List[List[str]],
        i: int,
        j: int,
        word: str,
        alredy: set,
        n: int,
        m: int,
    ):
        if (
            (i, j) in alredy
            or len(alredy) == len(word)
            or i < 0
            or i >= n
            or j < 0
            or j >= m
            or board[i][j] != word[len(alredy)]
        ):
            return

        alredy.add((i, j))
        self.find_word(board, i + 1, j, word, alredy, n, m)
        self.find_word(board, i - 1, j, word, alredy, n, m)
        self.find_word(board, i, j + 1, word, alredy, n, m)
        self.find_word(board, i, j - 1, word, alredy, n, m)
        if len(alredy) < len(word):
            alredy.remove((i, j))


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word = "ABCESEEEFS"
    print(Solution().exist(board, word))

    # A B C E
    # S F E S
    # A D E E
