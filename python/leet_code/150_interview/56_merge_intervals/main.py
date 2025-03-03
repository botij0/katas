from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        r = []
        intervals.sort()
        print(intervals)
        start = intervals[0][0]
        end = intervals[0][-1]
        for i in range(0, len(intervals) - 1):
            if end >= intervals[i + 1][0]:
                end = intervals[i + 1][-1] if intervals[i + 1][-1] >= end else end
                start = start if start <= intervals[i + 1][0] else intervals[i + 1][0]
            else:
                r.append([start, end])
                start = intervals[i + 1][0]
                end = intervals[i + 1][-1]
        r.append([start, end])
        return r


if __name__ == "__main__":
    intervals = [[1, 4], [4, 5]]
    print(Solution().merge(intervals))
