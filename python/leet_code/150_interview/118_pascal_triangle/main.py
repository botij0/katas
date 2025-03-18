from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        last = []
        r = []
        for i in range(1, numRows + 1):
            current = [1] * i
            if i > 2:
                for j in range(1, len(current) - 1):
                    current[j] = last[j - 1] + last[j]
            r.append(current)
            last = current
        return r


if __name__ == "__main__":
    numRows = 1
    print(Solution().generate(numRows))
