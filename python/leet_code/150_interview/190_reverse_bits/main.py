class Solution:
    def reverseBits(self, n: int) -> int:
        x = bin(n)
        r = "".join(reversed(x))
        r = r[:-2]
        if len(r) < 32:
            r += "0" * (32 - len(r))
        return int(r, 2)


if __name__ == "__main__":
    n = 43261596
    print(Solution().reverseBits(n))
