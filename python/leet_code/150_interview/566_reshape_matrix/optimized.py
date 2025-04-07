from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        def get_mat_nums(m: int, n: int):
            nums = []
            for i in range(m):
                for j in range(n):
                    nums.append(mat[i][j])
            return nums[::-1]

        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        aux = []
        nums = get_mat_nums(m, n)
        for _ in range(r):
            row = []
            for _ in range(c):
                row.append(nums.pop())
            aux.append(row)

        return aux


if __name__ == "__main__":
    mat = [[1, 2], [3, 4]]
    r = 2
    c = 4
    print(Solution().matrixReshape(mat, r, c))
