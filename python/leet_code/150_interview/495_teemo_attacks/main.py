from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        s = set(timeSeries)
        is_poissoned = duration
        count = 0
        for i in range(timeSeries[0], timeSeries[-1] + 2):
            if i in s:
                is_poissoned = duration

            if is_poissoned != 0:
                is_poissoned -= 1
                count += 1

        return count + is_poissoned


if __name__ == "__main__":
    timeSeries = [1, 4]
    duration = 2
    print(Solution().findPoisonedDuration(timeSeries, duration))
