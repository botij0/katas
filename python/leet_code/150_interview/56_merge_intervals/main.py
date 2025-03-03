from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        r = []
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][-1]

        for i in range(0, len(intervals) - 1):
            current_start, current_end = intervals[i + 1]

            if end >= current_start:
                end = current_end if current_end >= end else end
                start = start if start <= current_start else current_start

            else:
                r.append([start, end])
                start = current_start
                end = current_end

        r.append([start, end])
        return r


if __name__ == "__main__":
    intervals = [[1, 4], [4, 5]]
    print(Solution().merge(intervals))
