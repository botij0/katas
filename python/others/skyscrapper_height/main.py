from typing import List


class Solution:
    def solution(self, A: List[int]) -> List[int]:
        skyscrapper = set()
        for i in range(len(A)):
            A[i] = self.get_max_height(skyscrapper, A[i])
        return A

    def get_max_height(self, skyscrapper: set, current_height: int) -> int:
        if current_height not in skyscrapper:
            skyscrapper.add(current_height)
            return current_height
        else:
            return self.get_max_height(skyscrapper, current_height - 1)

    # Evita el posible desbordamiento de Pila
    def solution2(self, A: List[int]) -> List[int]:
        skyscrapper = set()

        for i in range(len(A)):
            height = A[i]

            while height in skyscrapper:
                height -= 1

            skyscrapper.add(height)
            A[i] = height

        return A


if __name__ == "__main__":
    A = [9, 4, 3, 7, 7]
    print(Solution().solution(A))
