class Solution:
    def hammingWeight(self, n: int) -> int:
        b_number = bin(n)
        b_number = b_number[2:]
        return b_number.count("1")


if __name__ == "__main__":
    n = 11
    print(Solution().hammingWeight(n))
