class Solution:
    def mySqrt(self, x: int) -> int:
        # Clasic Binary Search
        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1

        return left - 1


if __name__ == "__main__":
    x = 8
    print(Solution().mySqrt(x))
