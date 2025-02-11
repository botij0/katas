from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0


if __name__ == "__main__":
    citations = [1, 7, 9, 4]
    print(Solution().hIndex(citations))
