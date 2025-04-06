class Solution:
    def reverseWords(self, s: str) -> str:
        aux = s.split()
        s = ""
        for w in aux:
            s += "".join(reversed(w))
            s += " "

        return s[:-1]


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print(Solution().reverseWords(s))
