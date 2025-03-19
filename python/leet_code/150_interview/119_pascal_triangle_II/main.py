from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        last = []
        for i in range(1, rowIndex + 2):
            current = [1] * i
            for j in range(1, len(current) - 1):
                current[j] = last[j - 1] + last[j]

            last = current

        return last


if __name__ == "__main__":
    rowIndex = 1
    print(Solution().getRow(rowIndex))
