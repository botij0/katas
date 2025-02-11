from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return self.get_count_of_n(citations, len(citations))

    def get_count_of_n(self, citations: List[int], n: int) -> int:
        count = 0
        for cit in citations:
            if cit >= n:
                count += 1

        if count >= n:
            return n

        return self.get_count_of_n(citations, n - 1)


if __name__ == "__main__":
    citations = [1, 7, 9, 4]
    print(Solution().hIndex(citations))
