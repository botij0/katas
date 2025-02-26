class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        s = s.strip()
        current_word = ""
        for c in s:
            if c == " ":
                if len(current_word) > 0:
                    words.append(current_word)
                current_word = ""
            else:
                current_word += c
        if len(current_word) > 0:
            words.append(current_word)
        words.reverse()
        return " ".join(words)


if __name__ == "__main__":
    s = "a good   example"
    aux = Solution().reverseWords(s)
    print(aux, len(aux))
