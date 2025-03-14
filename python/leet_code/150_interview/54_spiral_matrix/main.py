from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = []
        while matrix:
            self.get_row_and_rotate(matrix, r)

        return r

    def get_row_and_rotate(self, matrix: List[List[int]], r: List[int]):
        for n in matrix[0]:
            r.append(n)

        # delete appended row
        matrix[:] = matrix[1::]

        # Rotate -90
        matrix[:] = [list(row) for row in zip(*matrix)][::-1]


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(Solution().spiralOrder(matrix))
