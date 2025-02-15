from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        last_candies = 0
        s_candies = 0
        n = len(ratings)
        for i in range(n):
            s_candies += 1

            if n > 1 and i == 0:
                if ratings[i] > ratings[i + 1]:
                    last_candies = self.find_next_max(ratings[i + 1 :], ratings[i])
                    s_candies += last_candies

            else:
                if ratings[i] > ratings[i - 1]:
                    if i != n - 1:
                        if ratings[i] <= ratings[i + 1]:
                            last_candies += 1
                            s_candies += last_candies
                        else:
                            aux_candies = self.find_next_max(
                                ratings[i + 1 :], ratings[i]
                            )
                            aux2_candies = last_candies + 1
                            last_candies = max(aux_candies, aux2_candies)
                            s_candies += last_candies
                    else:
                        last_candies += 1
                        s_candies += last_candies

                elif i != n - 1:
                    if ratings[i] == ratings[i + 1]:
                        continue
                    elif ratings[i] > ratings[i + 1]:
                        last_candies = self.find_next_max(ratings[i + 1 :], ratings[i])
                        s_candies += last_candies
                    else:
                        last_candies = 0
        return s_candies

    def find_next_max(self, ratings, m):
        r = 0
        last = m
        for n in ratings:
            if n >= m or last <= n:
                break
            last = n
            r += 1

        return r


if __name__ == "__main__":
    ratings = [1, 3, 2, 2, 1]
    print(Solution().candy(ratings))
