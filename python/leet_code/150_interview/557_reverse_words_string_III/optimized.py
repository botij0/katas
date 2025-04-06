class Solution:
    def reverseWords(self, s: str) -> str:
        aux = []
        for w in s.split():
            aux.append(w[::-1])
        return " ".join(aux)


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print(Solution().reverseWords(s))
