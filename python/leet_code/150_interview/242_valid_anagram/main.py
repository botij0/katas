class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        x = {}
        f = True
        for c in s:
            if c not in x:
                x[c] = 1
            else:
                x[c] += 1

        for c in t:
            if c not in x:
                f = False
            else:
                x[c] -= 1
                if x[c] < 0:
                    f = False

        return f


if __name__ == "__main__":
    s = "rat"
    t = "cat"
    print(Solution().isAnagram(s, t))
