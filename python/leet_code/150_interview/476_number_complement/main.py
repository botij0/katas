class Solution:
    def findComplement(self, num: int) -> int:
        # My Method:
        # n = len(bin(num)) - 2
        # aux = int("1" * n, 2)
        # return num ^ aux

        # Leet Code method
        n = num.bit_length()
        aux = ~(~0 << n)
        return num ^ aux


if __name__ == "__main__":
    num = 8
    print(Solution().findComplement(num))
