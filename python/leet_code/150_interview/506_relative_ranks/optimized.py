from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = sorted(score, reverse=True)
        aux = {}
        for i in range(len(s)):
            if i == 0:
                aux[s[i]] = "Gold Medal"
            elif i == 1:
                aux[s[i]] = "Silver Medal"
            elif i == 2:
                aux[s[i]] = "Bronze Medal"
            else:
                aux[s[i]] = str(i + 1)
        r = []

        for n in score:
            r.append(aux[n])

        return r


if __name__ == "__main__":
    score = [10, 3, 8, 9, 4]
    print(Solution().findRelativeRanks(score))
