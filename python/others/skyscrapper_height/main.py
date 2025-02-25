from typing import List


class Solution:
    def solution(self, A: List[int]) -> List[int]:
        skyscrapper = []
        for n in A:
            self.get_max_height(skyscrapper, n)
        return skyscrapper

    def get_max_height(self, skyscrapper: list, current_height: int):
        if current_height not in skyscrapper:
            skyscrapper.append(current_height)
            return
        else:
            self.get_max_height(skyscrapper, current_height - 1)


if __name__ == "__main__":
    A = [9, 4, 3, 7, 7]
    print(Solution().solution(A))
