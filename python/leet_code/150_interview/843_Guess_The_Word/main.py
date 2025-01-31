class Master:
    def __init__(self, secret: str, allowedGuesses: int):
        self.secret = secret
        self.allowedGuesses = allowedGuesses

    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        r = 0
        for i in range(len(word)):
            if self.secret[i] == word[i]:
                r += 1
        return r


class Solution(object):
    def findSecretWord(self, words: list, master: Master):
        """
        :type words: List[Str]
        :type master: Master
        :rtype: None
        """
        tries = 0
        for word in words:
            if tries >= master.allowedGuesses:
                print("you failed")
                return

            x = master.guess(word)
            tries += 1

            if x == 6:
                print("You guessed the secret word correctly.")
        pass


if __name__ == "__main__":
    master = Master("acckzz", 10)
    words = ["acckzz", "ccbazz", "eiowzz", "abcczz"]
    Solution().findSecretWord(words, master)
