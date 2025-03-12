class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        prev1 = 1
        prev2 = 1
        cur = 0

        for _ in range(prev1, n):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur

        return cur


if __name__ == "__main__":
    n = 8
    print(Solution().climbStairs(n))

# 5
# 1 1 1 1 1
# 2 1 1 1
# 1 2 1 1
# 1 1 2 1
# 1 1 1 2
# 2 2 1
# 2 1 2
