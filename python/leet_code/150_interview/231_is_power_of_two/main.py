class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n % 2 != 0:
            return False

        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2

            if 2**mid > n:
                right = mid
            elif 2**mid < n:
                left = mid + 1
            else:
                return True
        return False


if __name__ == "__main__":
    n = 2147483646
    print(Solution().isPowerOfTwo(n))
