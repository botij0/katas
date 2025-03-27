class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return (bin(n).count("1")) == 1


if __name__ == "__main__":
    n = 16
    print(Solution().isPowerOfTwo(n))
