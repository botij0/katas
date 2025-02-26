from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        short_len = len(min(strs, key=len))
        index = short_len
        for j in range(short_len):
            for i in range(1, len(strs)):
                if strs[i][j] != first_word[j]:
                    if j < index:
                        index = j
                    break

        return first_word[:index]


if __name__ == "__main__":
    strs = ["dog", "racecar", "car"]
    # print(strs[0][:0])
    print(Solution().longestCommonPrefix(strs))
