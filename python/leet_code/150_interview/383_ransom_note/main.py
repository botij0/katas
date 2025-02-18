class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = set(ransomNote)
        for c in chars:
            if magazine.count(c) < ransomNote.count(c):
                return False

        return True


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"
    print(Solution().canConstruct(ransomNote, magazine))
