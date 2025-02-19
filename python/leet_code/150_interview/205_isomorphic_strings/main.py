class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        iso = {}
        for i in range(len(s)):
            if s[i] not in iso:
                if t[i] in iso.values():
                    return False

                iso[s[i]] = t[i]
            elif iso[s[i]] != t[i]:
                return False

        return True


if __name__ == "__main__":
    s = "badc"
    t = "baba"
    print(Solution().isIsomorphic(s, t))
