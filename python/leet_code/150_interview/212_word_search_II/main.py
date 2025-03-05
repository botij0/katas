from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        node = trie.root
        m = len(board)
        n = len(board[0])

        for w in words:
            trie.insert(w)

        for i in range(m):
            for j in range(n):
                self.find_word(board, node, i, j, "", res, m, n)

        return res

    def find_word(
        self,
        board: List[List[str]],
        node: TrieNode,
        i: int,
        j: int,
        path: str,
        res: List[str],
        m: int,
        n: int,
    ):
        if node.is_end:
            res.append(path)
            node.is_end = False  # Word alredy added so updated to false

        if i < 0 or i >= m or j < 0 or j >= n:
            return

        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return

        board[i][j] = "#"
        self.find_word(board, node, i + 1, j, path + tmp, res, m, n)
        self.find_word(board, node, i - 1, j, path + tmp, res, m, n)
        self.find_word(board, node, i, j + 1, path + tmp, res, m, n)
        self.find_word(board, node, i, j - 1, path + tmp, res, m, n)
        board[i][j] = tmp


if __name__ == "__main__":
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    print(Solution().findWords(board, words))
