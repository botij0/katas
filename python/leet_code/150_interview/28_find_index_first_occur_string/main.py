class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        end = 0
        current = 0
        n = len(haystack)
        m = len(needle)

        if m > n:
            return -1

        for i in range(n):
            if haystack[i] == needle[current]:
                start = i
                end = i + 1
                current += 1

                for j in range(end, n):
                    if current == m:
                        return start

                    if haystack[j] != needle[current]:
                        break
                    else:
                        current += 1

                if current == m:
                    return start

                current = 0

        return -1


if __name__ == "__main__":
    haystack = "a"
    needle = "a"
    print(Solution().strStr(haystack, needle))
