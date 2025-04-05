from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        aux = sorted(score, reverse=True)
        r = []

        for i in range(len(score)):
            x = aux.index(score[i])
            if x == 0:
                r.append("Gold Medal")
            elif x == 1:
                r.append("Silver Medal")
            elif x == 2:
                r.append("Bronze Medal")
            else:
                r.append(str(x + 1))

        return r


if __name__ == "__main__":
    score = [10, 3, 8, 9, 4]
    print(Solution().findRelativeRanks(score))
