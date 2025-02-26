class Solution:
    def solution(self, A: int, B: int) -> int:
        higher, lower = (A, B) if A >= B else (B, A)

        r1 = higher // 4
        r2 = higher // 3 if lower >= higher // 3 else 0
        r3 = lower // 2

        return max([r1, r2, r3])


if __name__ == "__main__":
    A = 1
    B = 8
    print(Solution().solution(A, B))
