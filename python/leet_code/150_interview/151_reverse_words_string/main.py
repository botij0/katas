class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word for word in s.split(" ") if word]
        return " ".join(reversed(words))


if __name__ == "__main__":
    s = "a good   example"
    aux = Solution().reverseWords(s)
    print(aux, len(aux))
