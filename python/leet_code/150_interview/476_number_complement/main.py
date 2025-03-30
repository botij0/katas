class Solution:
    def findComplement(self, num: int) -> int:
        n = len(bin(num)) - 2
        aux = int("1" * n, 2)
        return num ^ aux


if __name__ == "__main__":
    num = 8
    print(Solution().findComplement(num))
