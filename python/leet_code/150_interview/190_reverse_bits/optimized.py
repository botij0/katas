class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for i in range(32):
            bit = (n >> i) & 1
            rev |= bit << (31 - i)
        return rev


if __name__ == "__main__":
    n = 43261596
    print(Solution().reverseBits(n))
