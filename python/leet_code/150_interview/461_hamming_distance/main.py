class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")


if __name__ == "__main__":
    x = 1
    y = 4
    print(Solution().hammingDistance(x, y))
