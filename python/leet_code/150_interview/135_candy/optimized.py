from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        i = 1
        total = n

        while i < n:
            if ratings[i] == ratings[i - 1]:
                i += 1
                continue

            current_peak = 0
            while i < n and ratings[i] > ratings[i - 1]:
                current_peak += 1
                total += current_peak
                i += 1

            if i == n:
                return total

            current_valley = 0
            while i < n and ratings[i] < ratings[i - 1]:
                current_valley += 1
                total += current_valley
                i += 1

            total -= min(current_peak, current_valley)

        return total


if __name__ == "__main__":
    ratings = [1, 2, 4, 3, 2, 1]
    print(Solution().candy(ratings))
