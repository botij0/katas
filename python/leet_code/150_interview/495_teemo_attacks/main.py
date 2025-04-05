from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        last = timeSeries[0]
        total = duration
        for i in range(1, len(timeSeries)):
            if last + (duration - 1) >= timeSeries[i]:
                total += timeSeries[i] - last
            else:
                total += duration

            last = timeSeries[i]
        return total


if __name__ == "__main__":
    timeSeries = [1, 3, 5, 7, 9, 11, 13, 15]
    duration = 3
    print(Solution().findPoisonedDuration(timeSeries, duration))
