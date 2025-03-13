class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        current_letters = set()
        r = 0

        for right in range(0, len(s)):
            if s[right] not in current_letters:
                current_letters.add(s[right])
            else:
                if r < len(current_letters):
                    r = len(current_letters)
                while s[right] in current_letters:
                    current_letters.remove(s[left])
                    left += 1
                current_letters.add(s[right])

        if r < len(current_letters):
            r = len(current_letters)

        return r


if __name__ == "__main__":
    s = " "
    print(Solution().lengthOfLongestSubstring(s))
