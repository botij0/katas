from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        def get_mat_nums():
            nums = []
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    nums.append(mat[i][j])
            return nums[::-1]

        aux = []
        nums = get_mat_nums()
        try:
            for i in range(r):
                row = []
                for j in range(c):
                    row.append(nums.pop())
                aux.append(row)
        except IndexError:
            return mat

        return aux if len(nums) == 0 else mat


if __name__ == "__main__":
    mat = [[1, 2], [3, 4]]
    r = 2
    c = 4
    print(Solution().matrixReshape(mat, r, c))
